file_object = open() # parametri: filename + mode

from pathlib import path
path = path ('dir1', 'codice', 'myfile.txt')
f = open(path)
home = path.home()
path = path(home, 'dir1', 'codice', 'myfile.txt')
f = open(path)

file_object.close()

# capire python directory e open files: 
import os
os.getcwd()

# statement with e context manager per aprire file
with open ("myfile.txt") as f: #f = puntatore al file
  print(f.encoding)
  
text = f.read 
print text
text = f.read(33) #numero byte che voglio vedere 
print text

# metodo readline(): ritorna lista con linee di testo
with open ("myfile.txt", "rt") as f: # rt = metodo read: apre file in lettura 
  line = f.readline()
  print(line)
  
with open ("myfile.txt", "rt") as f:
  counter = 0 #contatore per numerare linee
  for line in f:
    counter += 1 
    print (f"{counter}: {line}") #per ogni iterazione visualizza linea nel terminale
    
# scrivere dati in forma binaria: bytes and bytearray
s = b'sequenza'
s = bytearray('sequenza', 'utf-8') #utf-8: formato per rappresentare caratteri unicode come sequenze variabili di singoli bytes
s.extend (b 'di bytes') # aggiunge elementi in coda

# encoding e decoding
x = 'sequenza'
y = x.encode ('utf-8') # metodo codifica oggetti text into byte
type(y)
# class bytes

x = b'sequenza'
y = x.decode('utf-8') # metodo decodofica oggetti bytes into text
type(y) 
# class str (text)

# metodo write() con text files 
file.write(str) # + modalita di apertura adatto (per scrivere file binario aggiungere b dopo la prima lettera della modalità di apertura)
# "w": write (scrittura in modo testo: file creato o sovrascritto)
# "a": append (scrittura in modo testo ma in accodamento: file creato o nuovi dati aggiunti in coda a preesistenti)
# "x": exclusive (file creato o generata eccezione impedendo sovrascrittura)
# "r+": read/write - aggironamento
# "w+": read/write - aggironamento
# "a+": append/read

with open("myfile.txt", "rt") as f_in, \
     open("outputfile.txt", "w") as f_out:
     lines = f_in.readlines() # letto file di test
     flag = True # se parte da false aggiunge solo righe pari 
     counter = 1 #imposta variabile booleana al valore T per determinare se inserire o meno la linea di testo nel file output
    for line in lines:
      if flag == True:
        f_out.write(f"{counter}:{line}") #quando il flag è true scrivo linea di testo nel file output con valore del contatore
      flag = not flag
      counter += 1 #nel loop inverto valore del flag da vero a falso e da falso a vero incrementando di 1 unita il contatore per inserire nel file output una riga si e una no
     
# metodi tell() e seek()




    
  

  
