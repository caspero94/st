import pymongo
from pymongo import  MongoClient

cluster = MongoClient("mongodb+srv://caspero:caspero@clustercrypto.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

db = cluster["CryptoData"]
collection = db["BTC/BUSD_1m"]


#insert period as a document inside our mongodb
def insert_period(period,incomes,expenses,comment):
    return collection.insert_one({"key":period,"incomes":incomes,"expenses":expenses,"comment":comment})

def fetch_all_periods():
    res = pd.DataFrame(list(collection.find().limit(10)))
    return res

def get_period(period):
  
    if not isinstance(period, dict):
        period = {"key": period}
    
    return collection.find(period)