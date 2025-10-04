import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import DREvent

# decoder function (already implemented)
def decoder(line: str, linecount, runnumber, nphys, nped, noth, ndisc):
    n = time.time()
    ev = DREvent.DRdecode(line, spec = '2025', verbose = False, dumperror = 'decerrors.txt')
    dt = 1000*(time.time()-n) # milliseconds
    nphys_ = nphys
    nped_ = nped
    noth_ = noth
    ndisc_ = ndisc
    if ev == None:
        print(f"Run {runnumber} line {linecount} - Event discarded")
        return nphys, nped, noth, ndisc+1
    if ev.TriggerMask == 0x1:
        nphys_ += 1
    elif True:
        nped_ += 1
    else:
        noth_ += 1
    adcs = len(ev.ADCs)
    tdcs = len(ev.TDCs)
    tdcs_good = len([t for t in ev.TDCs if ev.TDCs[t][1]])
    print(f"Run {runnumber} line {linecount:3d} - Event {ev.EventNumber:3d} Spill {ev.SpillNumber:3d} Trig {ev.TriggerMask} - {adcs} {tdcs} ({tdcs_good}) - counter: phys {nphys_:3d} ped {nped_:3d} oth {noth_:3d} disc {ndisc_:3d} - decoding time {dt:1.2f} ms") 
    return nphys_, nped_, noth_, ndisc_


class FileTailer(threading.Thread):
    """Thread that tails a file while it is being written."""
    def __init__(self, filepath, decoder):
        super().__init__(daemon=True)
        self.filepath = filepath
        self.decoder = decoder
        self.nphys = 0
        self.nped = 0
        self.noth = 0
        self.ndisc = 0

    def run(self):
        with open(self.filepath, "r") as f:
            linecount = 0
            while True:
                line = f.readline()
                if line:
                    self.nphys, self.nped, self.noth, self.ndisc = self.decoder(line, linecount, "<tbd>", self.nphys, self.nped, self.noth, self.ndisc)
                    linecount +=1
                else:
                    time.sleep(0.5)  # wait for new data
                if line and linecount % 10 == 0 and linecount > 0:
                    print(f'{time.ctime()} Still reading {self.filepath}')

class NewFileHandler(FileSystemEventHandler):
    def __init__(self, decoder):
        super().__init__()
        self.decoder = decoder

    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            tailer = FileTailer(event.src_path, self.decoder)
            tailer.start()


def watch_directory(path, decoder):
    event_handler = NewFileHandler(decoder)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f"Watching directory: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    watch_directory(sys.argv[1], decoder)
