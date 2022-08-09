# STATEMENT
s = "python"

#test condizionale
if expression:
  suite
elif expression:
  suite
else expression:
  suite

#loop
while expression:
  suite
else:
  suite
#ex:
x = 0
while x < 3:
  print(x)
  x += 1 
# 0 1 2

while True: #loop infinito
  x = input ("Inserire una stringa")
  if x == 'stop':
    break #per uscire dal loop infinito
ptint(x)
#continue per rieseguire il loop

#iterazioni
myList = [1,2,3]
for i in myList:
  print(i)
#1,2,3

myDict = {'a': 1, 'b': 2, 'c': 3}
for i in myDict:
  print (i)
#a,b,c
for i in myDict.values():
  print(i)
#1,2,3
for i in myDict.items():
  print(i)
#a:1,b:2,c:3

# range(start,stop,step) function
for i in range (10,16,2):
  print(i)
#10,12,14

# LIST COMPREHENSION
numbers = [1,2,3,4,5,6,7,8,9]
newn = [n*n for n in numbers if n%2 == 1]
newn
# [1,9,25,49,81]

# DICT COMPREHENSION
a = "python"
b = {k : ord(k) for R in a}
b
#{'p':112, 'y':121...} ord() funzione che riporta valore numerico associato al carattere

# SET COMPREHENSION
a = "doppione"
c = {k for k in a}
c
#{'i','e','p','n','o','d'} -> no valori duplicati

# FUNCTIONS
def myFunc(a,b,c,d):
  print(a,b,c,d)
def myFunc(b=20, a=10, d=40, c=30)
myFunc
#10,20,30,40 -> ordine

def myFunc(*args):
  print(args)  # -> tupla
myFunc (1,2,3,4)
#(1,2,3,4)

def myFunc(a, b, *args):
  print(a, b, args)  # -> args dichiarato a dx
myFunc (1,2,3,4,5)
# 1,2 (3,4,5)

def myFunc(*kwargs):
  print(kwargs)  # -> raggruppa numero variabile di argomenti keyword in dizionario
myFunc (a=1, b=2, c=3)
myFunc
# {'a'=1, 'b'=2, 'c'=3}

# STATEMENT RETURN
def sum(a,b):
  return a + b
def sum(a,b):
  return
#none
def sum(a,b):
  c = a+b
#none

# CHIAMARE UNA FUNZIONE
#function_name (arguments)

def lista def (l1, l2 = [1,2,3,4,5]):
  l = []
  for x in l1:
    if not x in l2:
      l.append (x)
  return l

# FUNZIONI COME OGGETTI: FUNCTION TYPE
# funzioni nidificate
def outer (x,y):
  def sum (a,b):
    return a + b
  print(sum(x,y))
outer(10,5)
#15

# funzione come valore di ritorno
def outer():
  def inner(a,b):
    print(a+b)
  return inner
f = outer
f(10,5)
#15

# funzione come parametro
def sum (a,b):
  print(a+b)
def yFunc(f,x,y): #f funzione (oggetto), x,y parametri
  f(x,y)
myFunc (sum,10,5)
#15





  
