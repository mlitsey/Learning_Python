import os
import pymongo

myclient= pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['mydatabase']
mycol=mydb["customers"]
#mydict={"name":"John","address":"Louisville, KY"}
for x in mycol.find({},{"_id":0, "name":1}):
    print(x)

os.system("pause")