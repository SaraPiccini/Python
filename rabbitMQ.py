# scrivere producer in python
import pika
print("colegamento a RabbitMQ")
 # per connettere un applicazione a rabbit: stabilire connessione: crea oggetto che supporta parametri di connessione a rabbit e oggetto che rappresenta connessione - ricevere canale da connessione
params = pika.ConnectionParameteres(host="localhost") 
connection = pika.BlockingConnection(params)
channel = connection.channel()
 # creazione di coda per essere usata dai consumer per ricevere messaggi
channel.queue_declare(queue='worker_queue')
print("eseguito") #indicare connessione terminata
 # invia al broker tot messaggi creando loop infinito (while true)
i = 0
while True:
  message = str(i) # contatore come stringa
  i += 1
  channel.basic_publish(exchange='', #consegna messaggio a rabbit pubblicandolo su exchange chiedendo a oggetto channel di eseguire un basic publish
                        routing_key='working-queue', #definizione del binding
                        body=message)
  print("inviato messaggio % s", message)
  if i > 100_000:
    break #esegui test condizionale per chiudere loop infinito
connection.close() #chiudere connessione verso RabbitMQ

# scrivere consumer (worker) in python
 # scopo: rivere e vissualizzare messaggi sul terminale (3 finestre del terminale)
import pika
print("colegamento a RabbitMQ")
 # per connettere un applicazione a rabbit: stabilire connessione: crea oggetto che supporta parametri di connessione a rabbit e oggetto che rappresenta connessione - ricevere canale da connessione
params = pika.ConnectionParameteres(host="localhost") 
connection = pika.BlockingConnection(params)
channel = connection.channel()
 # creazione di coda per essere usata dai consumer per ricevere messaggi
channel.queue_declare(queue='worker_queue')
print("eseguito") #indicare connessione terminata
 # chiedere al canale di consumare i messaggi in modo base per gestirli
def callback(ch, method, properties, body):
  print("Ricevuto % s", % body)
channel.basic_consume(callback,
                      queue = 'worker_queue',
                      no_ack = True) #non garantiao a rabbit di aver ricevuto messaggio - ricevuta di ritorno utile in altri casi
channel.start_consuming() #workers si ferma
