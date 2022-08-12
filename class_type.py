# statement CLASS
class myClass:
  pass #statement

myobj = myClass() #crea istanza nella classe ereditando attributi della classe

# Attributi di classe: conduviso da tutte le istanze della classe
class myClass:
  myAttr = 10
myClass.myAttr
#10

# Attributi di istana: specifici per ciascuna istanza
class myClass:
  def myMethod(self):
    print(id(self))
    
class myClass:
  def setMessage(self,message):
    self.message = message
   def printMessage(self):
    print(self.message)
    
# attributo a livello di singola istanza
m1 = myClass()
m2 = myClass()
m1.setMessage('primo')
m2.setMessage('secondo')
m1.printMessage()
#primo
m2.printMessage()
#secondo

# costruttore delle classe: metodo INIT
class myClass:
  def__init__(self,message):
   self.message = message
  def printMessage(self):
    print(self.message)

# metodi di classe
class myClass():
  counter = 0
  def__init__(self):
    myClass.counter += 1
    
@classmethod
def istanze(cls):
  print(cls.counter)

m1 = myClass()
m2 = myClass()
m3 = myClass()
myClass.istanze()
#3

# STATIC METHOD
class myClass():
  @staticmethod
  def somma (a,b):
    return(a+b)
s = myClass.somma(10,5)
print(s)
#15

# INHERITANCE 
class AClass(BClass): #A sottoclasse di B
  pass

# funzione isinstance
m1 = AClass()
isinstance (m1, AClass)
# True
isinstance (m1, BClass)
# True

# OVERRIDE: ridefinire attributo in sottoclasse ma sovrascrive anche metodo corrispondente della superlcasse
class AClass(BClass):
  def printMessagge(self):
    print("AClass" + self.message)
    
m1 = AClass()
m1.setMessagge('py')
m1.printMessage() #invoca metodo di istanza
#AClass py

# funzione SUPER per accedere ai metodi delle superclassi dalle sottoclassi e per non sovrascrivere metodo superclasse
class AClass(BClass):
  def__init__(self, message, valore):
    super().__init__(message)
    self.valore = valore
    
m1 = AClass('p', 20)
m1.valore
#20
m1.printMessage()
#p

# INFORMATION HIDING
# def property
Class myClass():
  def __init__(self, my_attr):
    self.priv_attr = my_attr
  def get_attr(self):
    return self.priv_attr #metodo legge (getter)
  def set_attr(self):
    self.priv_attr = attr #metodo scrive (setter)
  attr = property(det_attr, set_attr)

obj = myClass('p')
obj.attr
# 'p'
obj.attr = 'prova'
obj.attr
# 'prova'
  
# PROPERTY DECORATOR
@property #per getter
@name.setter #per setter
  
Class myClass():
  def __init__(self, my_attr):
    self.__priv__attr = my_attr
@property
  def attr (self):
    return self.__priv_attr
@attr.setter
  def attr(self, my_attr):
    self.__priv_attr = my_attr
      
# Esempio:
Class ContoCorrente:
  def__init__(self, nome, conto, importo):
    self.nome=nome
    self.conto=conto
    self.saldo=importo
  def preleva (self,importo):
    self.saldo -= importo
  def deposita (self,importo):
    self.saldo += importo
  def descrizione(self):
    print(self.nome, self.conto, self.saldo)
 
c1 = Contocorrente("Alessandro", "10", 2000)
c1 = Contocorrente("Susanna", "20", 5000)
    
print(c1.__saldo) # -> errore: nascondi attributo saldo
@property
def saldo(self):
  return self.__saldo

@saldo.setter
def saldo(self.importo):
  self.preleva(self.__saldo)
  self.deposita(importo)

# superclasse conto: generalizzazione Conto Corrente
# prima del codice ContoCorrente
Class Conto:
  def__init__(self,nome,conto):
    self.nome = nome
    self.conto = conto
    
# modifica classe ContoCorrente per farla diventare sottoclasse di Conto:
class ContoCoreente(Conto)
super().__init__(nome,conto) #sposta nella superlcasse attributi

# gestore conti correnti
Class GestoreContiCorrenti:
  @staticmethod
  def bonifico(sorgente,destinazione,importo)
sorgente.preleva(importo)
destinazione.deposita(importo)
GestoreContiCorrenti.bonifico(c1,c2,300)

# EXCEPTIONS
def myFunc (a,b):
  return a//b

myFunc(10,0)
#ZeroDivisionError

# per gestire eccezioni:
# statement composto: TRY/EXCEPT
def f(x,y):
  return x//y
try:
  c = f(4,0)
except:
  print("ERRORE")
#or
except ZeroDivisionError:
  print("ERRORE")
except IndexError:
  print("IndexError")

# statement TRY/EXCEPT/AS
def f(x,y):
  return x//y
try:
  c = f(4,0)
except ZeroDivisionError as e:
  print (e.args)
  
# clausole FINALLY - ELSE
try:
  suite
finally:
    suite #azione sempre eseguita anche se clausola try da errore

try:
  suite
except expression:
  suite
else:
  suite #eseguita solo se non viene sollevata nessuna eccezione nella try

# statement RAISE - ASSERT
for i in range(50):
  print(i)
  raise IndexError
  #or
  raise IndexError("Errore nel loop")
  #or
  raise #solleva eccezione interrompendo esecuzione

# per valutare se espressione è true or false (-> solleva eccezione)
assert expression, argument # stringa con messaggio
x = 10
assert x == 5, "valori diversi"
# AssertionError: valori diversi (eccezione + argomento aggiunto)






    
    
    
    
  
