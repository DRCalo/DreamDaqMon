# DreamDaqMon
Data monitor for DreamDaq

- `python2/` directory contains code for DreamDaq data monitoring as used at the 2023 test-beam on pcdreamus
- `DREvent.py` is a python3 version of the DREvent class to be used with TBDataPreparation at the 2023 test-beam via git-submodules
- AdcMap24.py contains a python version of the mapping between channels and ADC for the 2024 test beam. This is usually produced in python2. To convert it into a python3 file, you can use the command "2to3 -W -n your_script.py". This map can then be converted to Json using scripts in the 2024_SPS/scripts directory to be used within the C++ offline environment for teh correct mapping of the channels.


## Updated DREvent and 2025 data format
- 2025 data decoding is done on 32-bit raw data dumped on ASCII file. Every line of the file is passed to `DRdecode` with parameter `DRdecode(line, spec = '2025')`
- The decoding is done with library implemented in `decode_utils.py`, imported into `DREvent.py`. According to a predefined set of errors in the data structures, the decoding of an event may be continued, stopped or aborted
   - For non critical errors, the `DREvent` is filled with event information and ADC and TDC values
   - For critical errors, `DRdecode()` returns `None`. Use this to skip the event.
- A `main` is defined in `DREvent.py` for testing purpose: use it as `python DREvent.py <file> [v/vv]`. This calls `DRdecode(.. , dumperror = 'drevent_error_dump.txt')`; in the dump, complete information can be found to track the decoding errors encountered.
- The `DREvent` class memebers are the same as previous years. To be noted:
   - `triggermas` is 1 (`0b01`) for physics event and 2 (`0b10`) for pedestal events
   - `NumOfPhysEv`, `NumOfPedeEv` and `NumOfSpilEv` are filled with dummy `-1` in 2025 (i.e. there are no separate counters for physics and pedestal events in the data stream: it can be done offline based on the trigger mask)
- The `DREvent` clsss is compatible with both python2.7 and python3.8


## Other utilities
- `watch_daq.py` can be used to watch and decode new files written synchronously in a configurable directory path. It prints meaningful information on screen and it dumps events with errors. It works in python3 only
