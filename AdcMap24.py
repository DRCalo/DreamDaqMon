# ADC mapping for test beam 2024
# Author: Andrea.Negri@cern.ch

from collections import OrderedDict

# Mapping document
adcMapUrl="https://twiki.cern.ch/twiki/bin/view/DREAM/DreamTBAugust2024HW"

# Class describing an ADC channel
class ADC:
  ''' Class describing and ADC channel, i.e.
    - addr     # channel address in the raw data format (0-31 first ADC, 32-63 second ADC ...)
    - module   # name of the calorimeter module
    - ringId   # 10*ringNumber + canvasPosition (1...9); it's -1 for not calo channels
    - pedestal # pedestal # pedestal value
  '''
  def __init__(self, addr, module, ringId=-1, pedestal=0):
    self.addr     = addr     # channel address in the raw data format (0-31 first ADC, 32-63 second ADC ...)
    self.module   = module   # name of the calorimeter module
    self.ringId   = ringId   # 10*ringNumber + canvasPosition (1...9); it's -1 for not calo channels
    self.pedestal = pedestal # pedestal value
 
  def __str__(self):
    return "%4d %8s %4d %4d " % (self.addr, self.module, self.ringId, self.pedestal)

  def to_dict(self):
    return {
      'addr':self.addr,
      'module':self.module,
      'ringId':self.ringId,
      'pedestal':self.pedestal
      }

# ADC map
#  - key:   Physical Channel Name, ie: name of the channel for reconstruction
#  - value: object of class ADC
adcMapDictionary = OrderedDict([
  # S-Channels
  ( "TS55", ADC(  3, "M1-S4", 41, 0 ) ),  ( "TS54", ADC(  7, "M2-S4", 42, 0) ),  ( "TS53", ADC( 11, "M3-S4", 43, 0) ),    # <--- Ring 4
  ( "TS45", ADC(  2, "M1-S3", 31, 0 ) ),  ( "TS44", ADC(  6, "M2-S3", 32, 0) ),  ( "TS43", ADC( 10, "M3-S3", 33, 0) ),    # <--- Ring 3
  ( "TS35", ADC(  1, "M1-S2", 21, 0 ) ),  ( "TS34", ADC(  5, "M2-S2", 22, 0) ),  ( "TS33", ADC(  9, "M3-S2", 23, 0) ),    # <--- Ring 2
  ( "TS25", ADC(  0, "M1-S1", 11, 0 ) ),  ( "TS24", ADC(  4, "M2-S1", 12, 0) ),  ( "TS23", ADC(  8, "M3-S1", 13, 0) ),    # <--- Ring 1
  ( "TS16", ADC( 15, "M4-S4",  1, 0 ) ),  ( "TS15", ADC( 19, "M5-S4",  2, 0) ),  ( "TS14", ADC( 23, "M6-S4",  3, 0) ),    # <--\ 
  ( "TS17", ADC( 14, "M4-S3",  4, 0 ) ),  ( "TS00", ADC( 18, "M5-S3",  5, 0) ),  ( "TS13", ADC( 22, "M6-S3",  6, 0) ),    # <--- Ring 0
  ( "TS10", ADC( 13, "M4-S2",  7, 0 ) ),  ( "TS11", ADC( 17, "M5-S2",  8, 0) ),  ( "TS12", ADC( 21, "M6-S2",  9, 0) ),    # <--/ 
  ( "TS20", ADC( 12, "M4-S1", 17, 0 ) ),  ( "TS21", ADC( 16, "M5-S1", 18, 0) ),  ( "TS22", ADC( 20, "M6-S1", 19, 0) ),    # <--- Ring 1
  ( "TS30", ADC( 27, "M7-S4", 27, 0 ) ),  ( "TS31", ADC( 31, "M8-S4", 28, 0) ),  ( "TS32", ADC( 64, "M9-S1", 29, 0) ),    # <--- Ring 2
  ( "TS40", ADC( 26, "M7-S3", 37, 0 ) ),  ( "TS41", ADC( 30, "M8-S3", 38, 0) ),  ( "TS42", ADC( 65, "M9-S2", 39, 0) ),    # <--- Ring 3
  ( "TS50", ADC( 25, "M7-S2", 47, 0 ) ),  ( "TS51", ADC( 29, "M8-S2", 48, 0) ),  ( "TS52", ADC( 66, "M9-S3", 49, 0) ),    # <--- Ring 4
  ( "TS60", ADC( 24, "M7-S1", 57, 0 ) ),  ( "TS61", ADC( 28, "M8-S1", 58, 0) ),  ( "TS62", ADC( 67, "M9-S4", 59, 0) ),    # <--- Ring 5
                                                                                             
  # C-Channels
  ( "TC55", ADC( 35, "M1-C4", 41, 0 ) ),  ( "TC54", ADC( 39, "M2-C4", 42, 0) ),  ( "TC53", ADC( 43, "M3-C4", 43, 0) ),    # <--- Ring 4
  ( "TC45", ADC( 34, "M1-C3", 31, 0 ) ),  ( "TC44", ADC( 38, "M2-C3", 32, 0) ),  ( "TC43", ADC( 42, "M3-C3", 33, 0) ),    # <--- Ring 3
  ( "TC35", ADC( 33, "M1-C2", 21, 0 ) ),  ( "TC34", ADC( 37, "M2-C2", 22, 0) ),  ( "TC33", ADC( 41, "M3-C2", 23, 0) ),    # <--- Ring 2
  ( "TC25", ADC( 32, "M1-C1", 11, 0 ) ),  ( "TC24", ADC( 36, "M2-C1", 12, 0) ),  ( "TC23", ADC( 40, "M3-C1", 13, 0) ),    # <--- Ring 1  
  ( "TC16", ADC( 47, "M4-C4",  1, 0 ) ),  ( "TC15", ADC( 51, "M5-C4",  2, 0) ),  ( "TC14", ADC( 55, "M6-C4",  3, 0) ),    # <--\ 
  ( "TC17", ADC( 46, "M4-C3",  4, 0 ) ),  ( "TC00", ADC( 50, "M5-C3",  5, 0) ),  ( "TC13", ADC( 54, "M6-C3",  6, 0) ),    # <--- Ring 0
  ( "TC10", ADC( 45, "M4-C2",  5, 0 ) ),  ( "TC11", ADC( 49, "M5-C2",  8, 0) ),  ( "TC12", ADC( 53, "M6-C2",  9, 0) ),    # <--/ 
  ( "TC20", ADC( 44, "M4-C1", 17, 0 ) ),  ( "TC21", ADC( 48, "M5-C1", 18, 0) ),  ( "TC22", ADC( 52, "M6-C1", 19, 0) ),    # <--- Ring 1
  ( "TC30", ADC( 59, "M7-C4", 27, 0 ) ),  ( "TC31", ADC( 63, "M8-C4", 28, 0) ),  ( "TC32", ADC( 68, "M9-C1", 29, 0) ),    # <--- Ring 2
  ( "TC40", ADC( 58, "M7-C3", 37, 0 ) ),  ( "TC41", ADC( 62, "M8-C3", 38, 0) ),  ( "TC42", ADC( 69, "M9-C2", 39, 0) ),    # <--- Ring 3
  ( "TC50", ADC( 57, "M7-C2", 47, 0 ) ),  ( "TC51", ADC( 61, "M8-C2", 48, 0) ),  ( "TC52", ADC( 70, "M9-C3", 49, 0) ),    # <--- Ring 4
  ( "TC60", ADC( 56, "M7-C1", 57, 0 ) ),  ( "TC61", ADC( 60, "M8-C1", 58, 0) ),  ( "TC62", ADC( 71, "M9-C4", 59, 0) ),    # <--- Ring 5

  # Ancillary
  ( "PreSh" , ADC( 72, "PreSh" ) ),
  ( "TailC" , ADC( 96, "TileC" ) ),
  ( "MuonT" , ADC( 97, "MuonT" ) ),
  ( "Cher1" , ADC(101, "Cher1" ) ), # Channel 98 no working 
  ( "Cher2" , ADC( 99, "Cher2" ) ),
  ( "Cher3" , ADC(100, "Cher3" ) ),

  #                                                            |Beam
  # Leakage counters                                           |
  # Bottom                          Left (Saleve)              V    Top                             Right (Jura)
  ( "L04", ADC(114, "Leak04" ) ), ( "L03", ADC(113, "Leak03" ) ),                                 ( "L02", ADC(112, "Leak02" ) ),
  ( "L09", ADC(118, "Leak09" ) ), ( "L08", ADC(117, "Leak08" ) ), ( "L07", ADC(116, "Leak07" ) ), ( "L05", ADC(115, "Leak05" ) ), 
  ( "L13", ADC(122, "Leak13" ) ), ( "L12", ADC(121, "Leak12" ) ), ( "L11", ADC(120, "Leak11" ) ), ( "L10", ADC(119, "Leak10" ) ),
  ( "L20", ADC(126, "Leak20" ) ), ( "L16", ADC(125, "Leak16" ) ), ( "L15", ADC(124, "Leak15" ) ), ( "L14", ADC(123, "Leak14" ) ),
])


# Class to access the adcMapDictionary
class AdcMap:
  '''Manage access to the ADC map '''

  def __init__(self, theDict):
    '''Constructor from the dictionary'''
    self.theDict=theDict 
    self.hCoordCache={}  # Time optimization
    self.pedeCache  ={}  # Time optimization

  def getADC(self, key):
    '''From key to value, i.e. the ADC class'''
    return self.theDict[key] 

  def getKey(self, val):
    '''From value (i.e. module name or address) to key (the channel name)'''
    for key, value in list(self.theDict.items()):
      if value.module == val or value.addr == val:
	return key

  def getPedestalFromAddress(self, addr):
    '''Get pedestal value from address'''
    if str(addr) in self.pedeCache: 
      return  self.pedeCache[str(addr)]
    key=self.getKey(addr)
    if key:
      self.pedeCache[str(addr)]=self.getADC(key).pedestal 
      return self.getADC(key).pedestal
    else  : return None

  def fromAddress2AdcBoardAndChannel(self, addr):
    '''Returns the tuple (AdcNumber, AdcChannel'''
    return addr / 32, addr % 32
  
  def fromAdcBoardAndChannel2Address(self, adc, ch):     
    '''Returns the raw channel address from the adc number and adc channel '''
    return adc*32 + ch
  
  def dumpByPhCh(self):
    '''Dump the dictionary ordered by name of the channel used in recostrution '''
    for key, value in sorted(self.theDict.items()):
      print(key, value)
  
  def dumpByAddr(self):
    '''Dump the dictionary ordered by raw address '''
    for key, value in sorted(list(self.theDict.items()), key=lambda x: x[1].addr):
      print(value, key)
  
  def dumpByModule(self, module):
    '''Dump the dictionary of a given module '''
    for key, value in sorted(list(self.theDict.items()), key=lambda x: x[1].module):
      if value.module.startswith(module):
        print(value, key)
  
  def ringAddr(self, ring, fiberType):
    '''Return list of adresses of a ring '''
    output = []
    if fiberType != "C" and fiberType != "S":
      return output 
    for key, value in list(self.theDict.items()):
      if value.ringId > 10*ring and value.ringId  < 10*(ring+1):
        if key.find(fiberType)>0:
          output.append(value.addr)
    return output

  def dumpMap(self, filt ):
    '''Dump formatted TC or TS map '''
    if filt != "TC" and filt != "TS":
      return  
    cnt = 1
    print("| PhyCh Addr Modul  | PhyCh Addr Modul  | PhyCh Addr Modul  |")
    print("------------------------------------------------------------")
    for key, value in list(self.theDict.items()):
      if key.startswith(filt):
        print("| %4s %4d %6s " % (key, value.addr, value.module), end=' ')
        if cnt%3 == 0:
          print("|")
        if cnt%12 == 0:
          print("------------------------------------------------------------")
        cnt=cnt+1
  
  def getAddresses(self, filt ):
    '''Dump formatted TC or TS map '''
    if filt != "TC" and filt != "TS":
      return  
    v = []
    for key, value in list(self.theDict.items()):
      if key.startswith(filt):
        v.append(value.addr)
    return v

 
  
  def getHistoMapCoord(self, filt, ch ):
    '''Return x,y histogram coordinate of channel ch'''
    if filt != "TC" and filt != "TS":
      return None
    if str(ch) in self.hCoordCache: 
      return  self.hCoordCache[str(ch)]
    cnt = -1
    found = False
    for key, value in list(self.theDict.items()):
      if key.startswith(filt):
        cnt+=1
        if value.addr == ch:
          found = True
          break
    if not found:
      return None
    column = -1 + cnt % 3
    row    = 11 - cnt // 3
    self.hCoordCache[str(ch)]=(column,row)
    return column, row


# Main for testing purpose
if __name__ == "__main__":
  aMap = AdcMap(adcMapDictionary)

  print("--------- From ADC values to key --------------------")
  print(aMap.getKey(22))
  print(aMap.getKey("M5-S3"))
  
  print("--------- From channel name to ADC ------------------")
  print(aMap.getADC("TS24"))
  print(aMap.getADC("TS24").addr)
   
  print("---------- From address to #ADC,#CH and vice versa --")
  print(aMap.fromAddress2AdcBoardAndChannel(37))
  print(aMap.fromAdcBoardAndChannel2Address(1,5))

  print("---------- From ADC value to ADC value --------------")
  key=aMap.getKey("M5-S3")
  print(aMap.getADC(key).addr)
  
  print("---------- getPedestalFromAddress --------------")
  print(aMap.getPedestalFromAddress(22))

  print("---------------- Dump by Physical channel -------------")
  aMap.dumpByPhCh()
  
  print("---------------- Dump by address ----------------------")
  aMap.dumpByAddr()
  
  print("---------------- Dump by module -----------------------")
  aMap.dumpByModule("M5")
  
  print("---------------- Return Ring Address ----------------------")
  ringAddresses = aMap.ringAddr(0, "C")
  print(ringAddresses)
  
  print("---------------- DumpMap ----------------------")
  aMap.dumpMap("TS")

  
  print("---------------- Get histogram coordinates  ---------------")
  print(aMap.getHistoMapCoord("TC", 39))
  print(aMap.getHistoMapCoord("TC", 60))
  print(aMap.getHistoMapCoord("TC", 160))

