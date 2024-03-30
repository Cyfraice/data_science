from pymongo import MongoClient
import pprint
import datetime

try:
    client = MongoClient()

except:
    print("connessione non riuscita")
#mi collego tramite socket di default al mongoDB

db = client.db
#creo un database e lo salvo

collezione = db.collezione
#creo una collezione e la salvo

collezione2 = db.collezione2

post = {   
    "nome" : "Giuseppe",
    "cognome" : "Gerolamo",
    "lista" : ["a","b"],
    "data" : datetime.datetime.now(tz=datetime.timezone.utc),
}
#crea un documento e lo salvo

collezione.insert_one(post)
#inserisco il documento nella collezione


collezione.insert_many([
    {
        "nome":"Giuseppe",
        "anni":21,
    },
    {
        "nome":"Luigi",
        "cognome":"Napoli",
        "altezza": 1.80,
    }
])
#inserisco più oggetti

x=collezione.delete_many({"nome":"Luigi"})
#cancello l'elemento che corrisponde al parametro specificato

a = db.list_collection_names()
#ottengo una lista dei nomi delle collezioni e le salvo

# pprint.pprint(collezione.find_one())
#stampo il primo documento della collezione

updateOne = (collezione.update_one({'commenti'},{"$set":{"nome":"Giulio"}}))
#modifico il primo elemento con chiave-valore specificato

updateMany = (collezione.update_many({"cognome":"Gerolamo"},{"$set":{"nome":"Gio"}}))
#modifico tutti gli elementi

collezione.find({"nome":"Gio"})
#cerco tutti gli elementi con con chiave "nome" e valore "Gio"


ini=collezione.find().limit(3)

#for o in ini:
    
    # pprint.pprint(o)
    # print("______")
#ciclo la lista degli oggetti con un limite e li stampo a schermo


dt = datetime.datetime(2023,10,18,14,10)

temp=collezione.find({"data": {"$lt": dt}})
#ho settato una data e cerco gli elementi della collezione salvati prima della data

for o in temp:
    
    pprint.pprint(o)
    print("______")
#ciclo la lista degli oggetti con un limite e li stampo a schermo


collezione2.insert_many([{
    "nome":"Giacomo",
    "cognome":"Bianchi",},
    {"nome":"Gio",
    "cognome":"Fre"}
    ])
#inserisco il documento nella seconda collezione

collezione.aggregate(collezione2)
#aggregazione tra due collezioni






x=collezione.delete_many({})
#print("Documenti eliminati: " + str(x.deleted_count))
#cancello tutti gli elementi

print("Collezioni:")
pprint.pprint(a)
#stampo i nomi delle collezioni presenti nel database

print("Documenti: ")
pprint.pprint(collezione.count_documents({}))
#conteggio di tutti i documenti nella collezione


print("Documenti eliminati: " + str(x.deleted_count))