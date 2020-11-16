import pymongo
def carregazoologico():

  # Define a new client.
  con_string = "mongodb+srv://gameplayer:Naotem99@cluster0.ci9ae.mongodb.net/"

  client = pymongo.MongoClient(con_string)
  mydb = client["savedgames"] #database

  db = mydb["bichos"] #document (table)
  zoologico = [ (x["bicho"],x["caracteristica"] )  for x in db.find({},{"_id":0,}) ]

  return zoologico