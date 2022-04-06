import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address" : "Park Lane 38"}
new_value = { "$set" : { "name" : "Ben da Silva"}}

mycol.update_one(myquery,new_value)

for x in mycol.find(myquery):
    print(x)