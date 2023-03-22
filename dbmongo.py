import pymongo
def get_mongo_db():
    # Configura tu conexión a la base de datos de MongoDB Atlas
    username = "casper"
    password = "caspero"
    cluster = "ClusterCrypto"
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

    # Selecciona la base de datos que deseas utilizar
    db = client["CryptoData"]

    return db
