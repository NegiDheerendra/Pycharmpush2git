import pymongo

client = pymongo.MongoClient("mongodb+srv://negidheerendra:ineuron1234@cluster0.hz0k4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
dict1={
    "id":1234,
    "name":"dheerendra",
    "email":"abc@gmail.com"
}
#changes in already written code
conn = client['mongotest']
coll=conn['test']
coll.insert_one(dict1)
