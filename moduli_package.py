import modulo1
modulo1.myFunc(10)
script1.py

def myFunc(x):
  print(x)
modulo1.py

import modulo1 as M
M.myFunc(10)

# statement FROM per importare solo alcuni attributi dal modulo
from modulo1 import myFunc
from modulo1 import* #tutti attributi singolarmente usati con il proprio nome direttamente - sconsigliato
from modulo1 import myFunc as f1 #per disambeguazione: da diversi modulo attributi con stesso nome

# attributo__name__
modulo1.__name__:
  "modulo1"
#or
"__main__"

if__name__=='__main__':
  myFunc(150) #trasforma modulo in script
  
#package
import dir_b.dirc_c.modulo1
from dir_b.dir_c.modulo1 import myFunc

# multiple inheritance
class AClass (BClass, CClass) :
  pass

a = AClass()
print(a.b)
print(a.c)
# method resolution order (MRO)

class myClass():
  def __new__ (cls): #costruttore di istanza di classe
    print ("Istanza creata")
  def __init__ (self): #inizializzatore di istanza di classe 
    print ("Istanza inizializzata")
    
class myClass():
  def __new__ (cls):
    istanza = super().__new__(cls)
    print ("Istanza creata")
    return istanza

# creazione iteratore
class myIter:
  def __iter__ (self): #oggetto iterabile che ritorna oggetto iteratore
    self.myattr = 2
    return self
  def __next__ (self): #oggetto iteratore che esegue iterazione su oggetti iterabili
    if self.myattr < 300:
      n = self.attr
      self.myattr* = 2
      return n
    else:
      raise stopiteration 

myClass = myIter()
myIter = iter (myClass)
for i in myIter:
  print(i)
  
# generator functions
def get_doppio_gen():
  e = 2
  while (e < 300):
    yield e #loop con variabile di controllo e e iteraotre con yield
    e *= 2 
    
gen = get_doppio_gen()
print(gen)
gen.__next__() #generator object

# return per interrompere funzione genertore e iterazione. eccezione: stopiteration 
def get_doppio_gen():
  e = 2
  while (True):
    yield e 
    e *= 2 
    if (e >= 300):
      return
gen = get_doppio_gen()
for e in gen():
  print(e)
  
# Generator expression equivalente a list comprehension, non puo essere iterato piu volte
list = [1,2,3,4,5]
newGen = (n*n for n in list if n % 2 == 1)
type(newGen)
# class generator
for e in newGen:
  print(e)
  

  
  
  


