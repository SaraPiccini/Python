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
