import pymongo
def salvabicho(animal):


  # Define a new client.
  con_string = "mongodb+srv://gameplayer:Naotem99@cluster0.ci9ae.mongodb.net/"

  client = pymongo.MongoClient(con_string)
  mydb = client["savedgames"] #database

  db = mydb["bichos"] #document (table)

  db.insert_one(animal)
  return 



