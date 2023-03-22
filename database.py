import pymongo
from pymongo import  MongoClient

cluster = MongoClient("mongodb+srv://caspero:caspero@clustercrypto.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

db = cluster["CryptoData"]
collection = db["BTC/BUSD_1m"]

def get_data():
    res = pd.DataFrame(list(collection.find().limit(10)))
    return res
