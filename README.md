# DreamDaqMon
Data monitor for DreamDaq

- `python2/` directory contains code for DreamDaq data monitoring as used at the 2023 test-beam on pcdreamus
- `DREvent.py` is a python3 version of the DREvent class to be used with TBDataPreparation at the 2023 test-beam via git-submodules
- AdcMap24.py contains a python version of the mapping between channels and ADC for the 2024 test beam. This is usually produced in python2. To convert it into a python3 file, you can use the command "2to3 -W -n your_script.py". This map can then be converted to Json using scripts in the 2024_SPS/scripts directory to be used within the C++ offline environment for teh correct mapping of the channels. 
