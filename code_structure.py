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



  
