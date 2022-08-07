# LIST TYPE
myList = [1,2,3,4]
myList = list()
myList.insert (2,8) #1,2,8,3,4
myList.append(6) #1,2,3,4,6
del myList[1] #1,3,4
2 in myList #True

myList2 = myList #una modifica in una lista si riflette anhe nell'altra
myList2 = myList.copy() #per lavorare in modo diverso su due liste uguali

# TUPLE TYPE
medaglie = ()
medaglie = 'oro', 'argento', 'bronzo'
medaglie = tuple()
# tuple unpaking
o,a,b = medaglie
o #'oro'
a #'argento'
b #'bronzo'

# DIZIONARI (key, value)
myDict{
   "primo": 10,
   "secondo": 20,
   "terzo" : 30
   } 
myDict = dict()
myDict["quarto"] = 40 #aggiungere elementi
del myDIct ["secondo"] #eliminare chiave e valore corrispondente
"terzo" in myDIct #True (solo per chiavi)

myDict2 = myDict
myDIct2 = myDict.copy()

# DICT.ITEMS
myDict.items() #crea lista con elementi tuple type
myDict.update() 

# SET TYPE (elementi univoci)
mySet = set()
mySet = ([10,20,30])
mySet = {10,20,30}
mySet = {} #crea dizionario vuoto, non set vuoto

mySet.add(10)
mySet = frozenset([10,20,30]) #crea set immutabili
30 in mySet #True

mySet2 = {30,40,50}
mySet & mySet2 #intersezione 30
mySet | mySet2 #unione 10,20,30,40,50
mySet - mySet2 #differenza 10,20
mySet ^ mySet2 #or esclusivo 10,20,40,50



