# Conversion fron ascii data format to DREvent class

import decode_utils as bob

class DREvent:
  ''' Class that represent a Dual Readout event at TB 2024 @H8 '''
  
  def __init__(self):
    ''' Constructor '''
    self.EventTime = ""
    self.EventNumber = 0
    self.SpillNumber = 0
    self.NumOfPhysEv = 0
    self.NumOfPedeEv = 0
    self.NumOfSpilEv = 0
    self.TriggerMask = 0
    self.ADCs = {}        # Simple dict      key(channel) : value
    self.TDCs = {}        # Dict key:tuple   key(channel) : ( value, check )

  def headLine(self):
    """Write header in ascii data dump"""
    return "%8s, %8s, %8s, %8s, %10s, %6s, %6s" % (
           "evNum", "#phEv", "#peEv", "#spEv", "trigM",
           "#ADCs", "#TDCs", )
  
  def __str__(self):
    """Overload of str operator (for data dump)"""
    return "%8d, %8d, %8d, %8d, 0x%08x, %6d, %6d" % (
          self.EventNumber, self.NumOfPhysEv, self.NumOfPedeEv, self.NumOfSpilEv, self.TriggerMask,
          len(self.ADCs), len(self.TDCs) )

  def getAdcChannel(self, ch):
    """get the data value for ADC channel ch"""
    return self.ADCs[ch]

  def getTdcChannel(self, ch):
    """get the data value for TDC channel ch"""
    return self.TDCs[ch]  # Tuple: (value, check)




# Parse the evLine and return a DREvent object -- Data format up to 2024
def DRdecode24(evLine):
  """Function that converts a raw data record (event) from
     ascii to object oriented representation: DREvent class"""
  # Create new DREvent
  e = DREvent()

  # Split sections
  strHeader  = evLine.split(":")[0]
  strPayload = evLine.split(":")[1]
  strPayload = strPayload.replace("TDC", ":TDC")
  strADCs    = strPayload.split(":")[0]
  strTDCs    = strPayload.split(":")[1]
	
  # Parse strHeader
  hList = strHeader.split()
  e.EventNumber = int( hList[2] )
  e.EventTime = hList[4]
  e.SpillNumber = int( hList[6] )
  e.NumOfPhysEv = int( hList[9] )
  e.NumOfPedeEv = int( hList[10] )
  e.NumOfSpilEv = int( hList[11] )
  try:
    e.TriggerMask = int( hList[14], 16 )
  except ValueError:
    print('ERROR: INVALID TRIGGER MASK: ' + hList[14]) 
    e.TriggerMask = 0xFFFFFFFF 
   
  # Parse ADC 
  listADCs = strADCs.split()
  for i in range(len(listADCs)):
    if i%2 ==0:
      ch = int(listADCs[i]  , 10)
      val= int(listADCs[i+1], 16)
      e.ADCs[ch]=val 

  # Parse TDC  
  entries  = -1
  try: entries  =  int(strTDCs.split()[2], 10)
  except ValueError: 
    # In the 1st runs the TCD size was exadecimal, then it was changed in decimal
    print("WARNING: TCD size not in decimal format, trying exadecimal")
    try: entries  =  int(strTDCs.split()[2], 16)
    except ValueError: 
      print ("WARNING: TCD size with unknown format.")
      pass
     

  strTDCs  = strTDCs[ strTDCs.find("val.s") + 6 : ]
  listTDCs = strTDCs.split()
  if entries > 0:
    for i in range(len(listTDCs)):
      if i%3 ==0:
        ch  = int( listTDCs[i+0], 10 )  # Channel
        ver = int( listTDCs[i+1], 10 )  # Varification number
        val = int( listTDCs[i+2], 10 )  # Value
        e.TDCs[ch] = ( val, ver) 
 
  return e


# Parse the evLine and return a DREvent object -- Raw data format since 
def DRdecode25(evLine, verbose):
  """Function that converts a raw data record (event) from
     ascii to object oriented representation: DREvent class"""
  # Create new DREvent
  e = DREvent()

  valid, header, adc, tdc = bob.decodeblock(evLine, verbose)

  
  if valid:
    try:
      evtnumber = header["evtnumber"]
    except:
      evtnumber = 0
    print("Evt %d - found decoding errors - %d ADCs %d TDCs decoded" %(evtnumber, len(adc), len(tdc)))
    for v in valid:
      print("Evt %d - error id %d: %s" %(evtnumber, v, bob.DecErr[v]))
    if bob.DiscardEvent(valid):
      print("Evt %d - discarding, returning None as event" %(evtnumber))
      return None

  # Parse header
  e.EventNumber = int( header["evtnumber"] )
  e.EventTime = header["evttime"]
  e.SpillNumber = int( header["spillnumber"] )
  e.NumOfPhysEv = int( header["nphys"] )
  e.NumOfPedeEv = int( header["nped"] )
  e.NumOfSpilEv = int( header["nevt"] )

  e.TriggerMask = int( header["trigmask"] )
  
  # Parse ADC 
  for chan in adc:
    e.ADCs[chan] = adc[chan]

  # TODO what is check number of TDCs? Setting to 1 now
  # Parse TDC
  for chan in tdc:
    e.TDCs[chan] = tdc[chan] # tdc[chan] is a pair (value, flag)

    
  return e

# Wrapper for compatibility with two data format
def DRdecode(evLine, spec='2025', verbose = False):

  if spec == '2025':
    return DRdecode25(evLine, verbose)
  else:
    if verbose:
      print('WARINIG - Verbosity implemented only for 2025 data format')
    return DRdecode24(evLine)


# Main for testing purpose
if __name__ == "__main__":
  import sys
  if len(sys.argv) < 2:
    print ("Usage: " + sys.argv[0] + " filename [v/vv=verbosity]")
    sys.exit(1)
 
  verboseHead = False
  verboseEvt = False
  if len(sys.argv) == 3:
    verboseHead = True
    if str(sys.argv[2]) == 'vv':
      verboseEvt = True
  for i, line in enumerate( open( sys.argv[1] ) ):
    ev = DRdecode(line, spec = '2025', verbose=verboseEvt)
    if verboseHead:
      if i%30 == 0:
        if ev != None:
          print(ev.headLine())
        else:
          print('None event')
        print(ev)
    

  
