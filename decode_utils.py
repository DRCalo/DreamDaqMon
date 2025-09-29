# decoding_utils.py
# Python 2 compatible (no dataclasses, no f-strings)

import re

DecErr = {1: "Invalid header",
          6: "Invalid trailer",
          2: "Invalid data spec 1",
          5: "Invalid data spec 4",
          999: "Invalid data type flag",
          111: "Channel already seen",
          254: "Unexpected 0xFE word"
          }

def _mask(n):
    return (1 << n) - 1 if n else 0

def _get_bits(v, start, size):
    """Extract 'size' bits starting at bit 'start' (0 = LSB)."""
    return (v >> start) & _mask(size)

def _u32(v):
    return v & 0xFFFFFFFF

# ---- Bit layouts (LSB -> MSB) ----------------------------------------------
# head_s:  u:8 | n:6 | z:2 | c:8 | m:3 | g:5
# trail_s: c:24 | m:3 | g:5
# data_s:  v:12 | f:3 | u:1 | c:8 | m:3 | g:5

def parse_head(hd, verb = False):
    hd = _u32(hd)
    u = _get_bits(hd, 0, 8)
    nch = _get_bits(hd, 8, 6)
    zero = _get_bits(hd, 14, 2)
    crate = _get_bits(hd, 16, 8)
    marker = _get_bits(hd, 24, 3)
    geo = _get_bits(hd, 27, 5)
    valid = 0 if marker == 2 else 254 if marker == 6 else 1
    if verb:
        print("header 0x%x geo %d marker %d crate %d zero %d chans %d not used %d - valid %d" % (hd, geo, marker, crate, zero, nch, u, valid))
    return valid, {"u": u, "n": nch, "z": zero, "c": crate, "m": marker, "g": geo, "raw": hd}

def parse_trail(tr, verb = False):
    tr = _u32(tr)
    c = _get_bits(tr, 0, 24)
    marker = _get_bits(tr, 24, 3)
    geo = _get_bits(tr, 27, 5)
    valid = 0 if marker == 4 else 6
    if verb:
        print("trail 0x%x geo %d marker %d event counter %d - valid %d" % (tr, geo, marker, c, valid))
    return valid, {"c": c, "m": marker, "g": geo, "raw": tr}

def parse_data(dt,spec = 1, verb = False): # 1 QDC,   4 TDC
    dt = _u32(dt)
    v = _get_bits(dt, 0, 12)
    f = _get_bits(dt, 12, 3)
    u = _get_bits(dt, 15, 1)  # "not used" in bob print
    c = _get_bits(dt, 16, 8)
    m = _get_bits(dt, 24, 3)
    g = _get_bits(dt, 27, 5)

    if spec == 1:
        chan = c & 0x1F
        flags = f & 0x3
        valid = 0 if m == 0 and flags == 0 else 2
        if verb:
            print("QDC index %d data 0x%x geo %d marker %d chan %d not used %d flags %d val %d - valid %d" % (spec, dt, g, m, chan, u, flags, v, valid))
    elif spec == 4:
        chan = ((c >> 1) & 0xF) & 0x1F
        flags = f
        valid = 0 if m == 0 and f == 0 else 0 # TODO
        if verb:
            print("TDC index %d data 0x%x geo %d marker %d chan %d not used %d flags %d val %d - valid %d" % (spec, dt, g, m, chan, u, flags, v, valid))
    else:
        return 999, {}
        
    return valid, {"v": v, "f": flags, "u": u, "c": chan, "m": m, "g": g, "raw": dt}




def decodeblock(line): # line is a single line string for one event. block is a list of 4-bytes words

    block = [int(i,16) for i in line.split()]

    valid = 0
    ADC = {}
    TDC = {}
    HEAD = {"evtnumber": 25, "evttime": "256-13-46-59-791534", "spillnumber": 1, "nphys": 25, "nped": 7, "nevt": 32, "trigmask": 0x5} # TODO placeholder
    adcset = set()
    tdcset = set()

    INDEX = 0
    nHeader = 0
    
    while INDEX < len(block):
        v, w = parse_head(block[INDEX])
        crate = w["c"]
        INDEX += 1
        if v == 254 and INDEX == len(block):  # 0xFE... words are tolerated at the end of the event
            return valid, HEAD, ADC, TDC
        elif v:
            return v, HEAD, {}, {}

        nHeader += 1
        for iword in range(w["n"]):
          
            isADC = (nHeader <= 5) # WIll be written in crate word
            v, w = parse_data(block[INDEX], spec = 1 if isADC else 4)
            INDEX += 1
            if v:
                return v, HEAD, {}, {}

            chan = (crate-1)*32 + w["c"]
            if isADC:
                if chan in adcset:
                    valid = 111
                adcset.add(chan)
                ADC[chan] = w["v"]
            else:
                if chan in tdcset:
                    valid = 111
                tdcset.add(chan)
                TDC[chan] = w["v"]

        v, w = parse_trail(block[INDEX])
        INDEX += 1
        if v:
            return v, HEAD, {}, {}

    return valid, HEAD, ADC, TDC

        

    
            
        
                

# ---- Optional: small demo when run directly ---------------------------------
if __name__ == "__main__":
    
    
    import sys
    if len(sys.argv) != 2:
        print("Usage: python2 %s <file>" % sys.argv[0])
        sys.exit(1)

    path = sys.argv[1]

    
    with open(path, "r") as f:
        evt = 0
        for line in f:
            line = line.strip()   # remove leading/trailing whitespace & newline
            print("--- Evt %d ---" %evt)
            evt += 1
            v, head, adc, tdc = decodeblock(line)
            if v:
                print("DECODING ERROR code %d : %s" %(v, DecErr[v]))
            else:
                print(adc)
                print(tdc)
