from pymongo import MongoClient
import streamlit as st
@st.cache_resource
def get_mongo_db():
    # Configura tu conexión a la base de datos de MongoDB Atlas
    username = "casper"
    password = "caspero"
    cluster = "ClusterCrypto"
    client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

    # Selecciona la base de datos que deseas utilizar
    db = client["CryptoData"]

    return db
