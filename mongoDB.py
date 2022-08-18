# rappresentazione oggeto in JSON
{
  "nome": "Mario",
  "cognome":"Rossi",
  "età":30
  "computer":{ 
    "comp1":"Asus",
    "comp2":"Apple"
  } #oggetto nidificato nell'oggetto
}

# array in JSON
{
  "nome": "Mario",
  "computer": ["Asus", "Apple"]
}

import pymongo
from pymongo import MongoClient

# connessione con MongoDB
client = Mongo Client('localhost', 27017) #porta

# creare database
db = client.testdb
#crea collection persone
persone_coll = db.persone

#crea indici per velocizzare accesso a dati
persone_coll.create_index([("nome", pymongo.ASCENDING)])
persone_coll.create_index([("cognome", pymongo.ASCENDING)])
persone_coll.create_index([("computer", pymongo.ASCENDING)])

#crea documento - dizionario
p1 = {"nome":"Mario", "cognome":"Rossi", "eta":30, "computer": ["Asus", "Apple"]}

#inserisci documento in mongodb
persone_coll.insert_one(p1)

#crea altro documento
p2 = {"nome":"Giuseppe", "cognome":"Verdi", "eta":45, "computer": ["Apple"]} #per omogeneità tutte le proprietà computer -> lista
persone_coll.insert_one(p2)

#accedi in lettura al databse creato creando nella stessa cartella il programma in python
#accedi a database e a collection persone

import pymongo
from pymongo import MongoClient

client = Mongo Client('localhost', 27017) #porta

db = client.testdb
persone_coll = db.persone

# accedi a info in mongodb
p = persone_coll.find_one()
print(p)

#ritorna documento con persone con computer apple
persone = persone_call.find({"computer": "Apple"})
for persona in persone:
  print(persona)
  
# modifica valore in una collezione con operatori: età verdi a 50 anni
res = persone_coll.update_one({"nome":"Giuseppe"}, {"$set": {"eta":50}})
p = persone_coll.find_one({"nome":"Giuseppe"})
print(p)

# trova il primo docuemnto in cui il primo nome > Giuseppe (condizione impostata attraverso filtro con operatore)
persona = persone_coll.find_one({"nome":{"$gt":"Giuseppe"}})
print(persona)

