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
  # Taken from https://twiki.cern.ch/twiki/bin/view/DREAM/DreamTBSeptember2025
  ( "105-S" , ADC(0,"105-S") ),
  ( "505-S" , ADC(32,"505-S") ),
  ( "105-C" , ADC(64,"105-C") ),
  ( "505-C" , ADC(96,"505-C") ),
  ( "L1" , ADC(128,"L1") ),
  ( "TailCatcher" , ADC(160,"TailCatcher") ),
  ( "106-S" , ADC(1,"106-S") ),
  ( "506-S" , ADC(33,"506-S") ),
  ( "106-C" , ADC(65,"106-C") ),
  ( "506-C" , ADC(97,"506-C") ),
  ( "L2" , ADC(129,"L2") ),
  ( "Muon" , ADC(161,"Muon") ),
  ( "107-S" , ADC(2,"107-S") ),
  ( "507-S" , ADC(34,"507-S") ),
  ( "107-C" , ADC(66,"107-C") ),
  ( "507-C" , ADC(98,"507-C") ),
  ( "L3" , ADC(130,"L3") ),
  ( "Cher1" , ADC(162,"Cher1") ),
  ( "108-S" , ADC(3,"108-S") ),
  ( "508-S" , ADC(35,"508-S") ),
  ( "108-C" , ADC(67,"108-C") ),
  ( "508-C" , ADC(99,"508-C") ),
  ( "L4" , ADC(131,"L4") ),
  ( "Cher2" , ADC(163,"Cher2") ),
  ( "109-S" , ADC(4,"109-S") ),
  ( "509-S" , ADC(36,"509-S") ),
  ( "109-C" , ADC(68,"109-C") ),
  ( "509-C" , ADC(100,"509-C") ),
  ( "L5" , ADC(132,"L5") ),
  ( "Cher3" , ADC(164,"Cher3") ),
  ( "110-S" , ADC(5,"110-S") ),
  ( "510-S" , ADC(37,"510-S") ),
  ( "110-C" , ADC(69,"110-C") ),
  ( "510-C" , ADC(101,"510-C") ),
  ( "L6" , ADC(133,"L6") ),
  ( "111-S" , ADC(6,"111-S") ),
  ( "511-S" , ADC(38,"511-S") ),
  ( "111-C" , ADC(70,"111-C") ),
  ( "511-C" , ADC(102,"511-C") ),
  ( "L7" , ADC(134,"L7") ),
  ( "112-S" , ADC(7,"112-S") ),
  ( "512-S" , ADC(39,"512-S") ),
  ( "112-C" , ADC(71,"112-C") ),
  ( "512-C" , ADC(103,"512-C") ),
  ( "L8" , ADC(135,"L8") ),
  ( "113-S" , ADC(8,"113-S") ),
  ( "513-S" , ADC(40,"513-S") ),
  ( "113-C" , ADC(72,"113-C") ),
  ( "513-C" , ADC(104,"513-C") ),
  ( "L9" , ADC(136,"L9") ),
  ( "114-S" , ADC(9,"114-S") ),
  ( "514-S" , ADC(41,"514-S") ),
  ( "114-C" , ADC(73,"114-C") ),
  ( "514-C" , ADC(105,"514-C") ),
  ( "L10" , ADC(137,"L10") ),
  ( "202-S" , ADC(10,"202-S") ),
  ( "402-S" , ADC(42,"402-S") ),
  ( "202-C" , ADC(74,"202-C") ),
  ( "402-C" , ADC(106,"402-C") ),
  ( "L11" , ADC(138,"L11") ),
  ( "203-S" , ADC(11,"203-S") ),
  ( "403-S" , ADC(43,"403-S") ),
  ( "203-C" , ADC(75,"203-C") ),
  ( "403-C" , ADC(107,"403-C") ),
  ( "L12" , ADC(139,"L12") ),
  ( "204-S" , ADC(12,"204-S") ),
  ( "404-S" , ADC(44,"404-S") ),
  ( "204-C" , ADC(76,"204-C") ),
  ( "404-C" , ADC(108,"404-C") ),
  ( "L13" , ADC(140,"L13") ),
  ( "205-S" , ADC(13,"205-S") ),
  ( "405-S" , ADC(45,"405-S") ),
  ( "205-C" , ADC(77,"205-C") ),
  ( "405-C" , ADC(109,"405-C") ),
  ( "L14" , ADC(141,"L14") ),
  ( "206-S" , ADC(14,"206-S") ),
  ( "406-S" , ADC(46,"406-S") ),
  ( "206-C" , ADC(78,"206-C") ),
  ( "406-C" , ADC(110,"406-C") ),
  ( "L15" , ADC(142,"L15") ),
  ( "207-S" , ADC(15,"207-S") ),
  ( "407-S" , ADC(47,"407-S") ),
  ( "207-C" , ADC(79,"207-C") ),
  ( "407-C" , ADC(111,"407-C") ),
  ( "L16" , ADC(143,"L16") ),
  ( "208-S" , ADC(16,"208-S") ),
  ( "408-S" , ADC(48,"408-S") ),
  ( "208-C" , ADC(80,"208-C") ),
  ( "408-C" , ADC(112,"408-C") ),
  ( "L17" , ADC(144,"L17") ),
  ( "209-S" , ADC(17,"209-S") ),
  ( "409-S" , ADC(49,"409-S") ),
  ( "209-C" , ADC(81,"209-C") ),
  ( "409-C" , ADC(113,"409-C") ),
  ( "L18" , ADC(145,"L18") ),
  ( "210-S" , ADC(18,"210-S") ),
  ( "410-S" , ADC(50,"410-S") ),
  ( "210-C" , ADC(82,"210-C") ),
  ( "410-C" , ADC(114,"410-C") ),
  ( "L19" , ADC(146,"L19") ),
  ( "211-S" , ADC(19,"211-S") ),
  ( "411-S" , ADC(51,"411-S") ),
  ( "211-C" , ADC(83,"211-C") ),
  ( "411-C" , ADC(115,"411-C") ),
  ( "L20" , ADC(147,"L20") ),
  ( "212-S" , ADC(20,"212-S") ),
  ( "412-S" , ADC(52,"412-S") ),
  ( "212-C" , ADC(84,"212-C") ),
  ( "412-C" , ADC(116,"412-C") ),
  ( "213-S" , ADC(21,"213-S") ),
  ( "413-S" , ADC(53,"413-S") ),
  ( "213-C" , ADC(85,"213-C") ),
  ( "413-C" , ADC(117,"413-C") ),
  ( "214-S" , ADC(22,"214-S") ),
  ( "414-S" , ADC(54,"414-S") ),
  ( "214-C" , ADC(86,"214-C") ),
  ( "414-C" , ADC(118,"414-C") ),
  ( "215-S" , ADC(23,"215-S") ),
  ( "415-S" , ADC(55,"415-S") ),
  ( "215-C" , ADC(87,"215-C") ),
  ( "415-C" , ADC(119,"415-C") ),
  ( "216-S" , ADC(24,"216-S") ),
  ( "416-S" , ADC(56,"416-S") ),
  ( "216-C" , ADC(88,"216-C") ),
  ( "416-C" , ADC(120,"416-C") ),
  ( "217-S" , ADC(25,"217-S") ),
  ( "417-S" , ADC(57,"417-S") ),
  ( "217-C" , ADC(89,"217-C") ),
  ( "417-C" , ADC(121,"417-C") ),
  ( "301-S" , ADC(26,"301-S") ),
  ( "314-S" , ADC(58,"314-S") ),
  ( "301-C" , ADC(90,"301-C") ),
  ( "314-C" , ADC(122,"314-C") ),
  ( "302-S" , ADC(27,"302-S") ),
  ( "315-S" , ADC(59,"315-S") ),
  ( "302-C" , ADC(91,"302-C") ),
  ( "315-C" , ADC(123,"315-C") ),
  ( "303-S" , ADC(28,"303-S") ),
  ( "316-S" , ADC(60,"316-S") ),
  ( "303-C" , ADC(92,"303-C") ),
  ( "316-C" , ADC(124,"316-C") ),
  ( "304-S" , ADC(29,"304-S") ),
  ( "317-S" , ADC(61,"317-S") ),
  ( "304-C" , ADC(93,"304-C") ),
  ( "317-C" , ADC(125,"317-C") ),
  ( "305-S" , ADC(30,"305-S") ),
  ( "318-S" , ADC(62,"318-S") ),
  ( "305-C" , ADC(94,"305-C") ),
  ( "318-C" , ADC(126,"318-C") ),
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

