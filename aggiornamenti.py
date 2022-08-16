# dizionari
# metodo keys: produce lisa con chiavi del dizionario con ordine preservato
myDict.keys()

# data annotations - supporto per data classes
def myFunc(x: "par x") -> "ritorno":
  return x
print(myFunc.__annotations__)
# {'x': 'par x', 'return': 'ritorno'}

# type hints - annotazione di tipo
def myFunc(x,s = "py"):
  print(x)
  return s
res = myFunc(10)
print(res)
#10 py

def myFunc(x: int,s: str = "py") -> str:
  print(x)
  return s
res = myFunc(10)
print(myFunc.__annotations__)
# {'x': class 'int','s': class 'str', 'return': class 'str'}

#syntax for variable annotations
a: int = 10
print(a)
print(__annotations__)
#{'a': class 'int'} 

# for classes
class myClass:
  nome: str
    cognome: str
      
      def __init__(self,nome,cognome):
        self.come = nome
        self.cognome = cognome
        
# decorator data classes aggiunge direttamente metodi: costruttore, metodo __repr__ per rappresentare contenuto istanza attraverso sue proprietà e operatori di confronto __eq__ (==), __ne__ (!=)
@dataclass
class myClass:
  nome: str
    cognome: str
# paramentri per personalizzar comportmento:
# init = True generato construttore - inizializza istanze
# repr = True - report (metodo)
# order = False metodi di confronto > <
# frozen = False possibilità di modificare valori di istnza

# Assignemnt expression: walrus operator :=
is (x := somma (5,3)) > 6:
  print (x>6)
# x>6
myList = [1,2,3]
while x := len (myList) != 0: #loop
    print (x, myList.pop()) #estrazione ultimo valore della lista
# True 3, true 2, true 1

# def saluta (nome = (n := "Susi")):

# parametri positional only
def somma (a,b,c):
  return a+b+c
x = somma (10,5,2) #positional arguments
y = somma (b=5, c=2, a=10) #keyward arguments, ordine diverso

def somma (a, /, b, c): # / divisore tra parametri positional only e gli altri
  return a+b+c
y = somma (10, c=2, b=5)

# union operaotrs per dizionari
myDict1 = {'a'='primo', 'b'='secondo'}
myDict2 = {'c'='terzo'}
# merge: copy() + loop per copiare valori + metodo .items() or with union operatore | and |=
myDict12 = myDict1 | myDict1
myDict1 |= myDict2

# metodi per rimuovere suffissi e prefissi da stringhe
lstrip() # rimozione caratteri a sx - usa insieme di caratteri non stringhe (re o er)
rstrip() # rimozione caratteri a dx - usa insieme di caratteri non stringhe (re o er)
strip() # rimozione caratteri a dx e sx e rimozione spazi - usa insieme di caratteri non stringhe (re o er)

removeprefix() #usa stringhe e non insieme di caratteri (solo re)
removesuffix #usa stringhe e non insieme di caratteri (solo re)

# pattern matching: verifica della presenza di pattern in oggetto composto
subject_value = ['primo', 'secondo']
match subject_value:
  case [p,s]:
    print(f"trovato {p} e {s}")

#capture patterns - catturano valori soggetti assegnandoli a variabili
subject_value = [1,2,3]
match subject_value:
  case [p,s]:
    print(f"trovato {p} e {s}") # match fallisce (solo 2 elementi)
   case [p,s,t]:
    print(f"trovato {p}, {s}, {t}") # realizza match

   case_:
    print ["case di default"] # quando nessuno dei pattern ha successo scatta questo che ha sempre successo

# literal paterns - match - confronto diretto di valori nel pattern
subject_value = [1,2,3]
match subject_value:
  case [1,2,3]:
    print(f"trovata lista 1,2,3")
  case [1, *resto]:
    print(f"il resto è {resto}")
# trovata lista 1,2,3
# il resto è [2,3]

# or patterns
subject_value = ['autunno', 'stagione autunnale']
match subject_value:
  case ['autunno', msg] | ['inverno', msg]: # | = or logico
    print(f"nella {msg} fa piu freddo")
# nella stagiona autunnale fa piu freddo

# as pattern
subject_value = 'estate'
match subject_value:
  case 'primavera' | 'estate' as stagione:
    print(f"in {stagione} fa piu caldo")
# in estate fa piu caldo

#conditional patterns
subject_value = ['pari', '50']
match subject_value:
  case ['pari', valore] if int (valore) %2 ==0:
    print(f" {valore} è un numero pari")
#50 è un numero pari
subject_value = ['pari', '50']
match subject_value:
  case ['pari', valore] if int (valore) %2 == 0:
    print(f" {valore} è un numero pari")
  case ['dispari', valore] if int (valore) %2 != 0:
    print(f" {valore} è un numero dispari")
  case_:
    print("c'è errore nei dati")
# c'è errore nei dati 


