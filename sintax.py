# linguaggio object-oriented
is-a # oggetto -> classe
kind-of # classe -> superclasse 
= # assegnamento 
== # testa se sono uguali

# test condizionale
def paridispari():
    inp = input("Inserisci un numero"):
    numero = int(inp)
    modulo = numero%2
    if modulo == 0:
       print("Numero Pari")
    else
       print("Numero Dispari")
paridispari()

x.y() #quando un attributo è una funzione

# F-string (formattazione testo)
%-formatting 
str.format()
f-string!
# Esempio - string interpolation: 
Titolo = Me
Autore = Te
f"Titolo: {titolo}, Autore: {autore}."
          titolo = Me, Autore = Te
          {titolo.upper()} = Me
          
#OPERATORI
+
-
*
/ # (floating-point)
// # (integer)
% # (modulo)
** # (esponenziale)
- # (meno unario: inverte segno)

# di assegnamento
=
+= # a += b equivale a a = a+b
-= 
# ...

# di confronto:
<
>
==
!=

# operatori logici
and 
or 
not # operatore unario

# operatori su sequenze (stringhe)
# indexing:
s = 'python'
s[0] # 'p'
s[3] # 'h'

#slicing:
s[:] # 'python'
s[-2:] # 'on'
s[1:5:2] # 'yo' (salta 2 caratteri tra il secondo e il sesto)

#concatenazione:
s = 'python'
r = 'programming'
t = s + r 
t #'python programming
       
