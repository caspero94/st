# Resources
import streamlit as st
import ccxt
from datetime import datetime
import pandas as pd
from pymongo import MongoClient

# Conecta a la base de datos
@st.cache(allow_output_mutation=True)
def get_mongo_db():
    # Configura tu conexión a la base de datos de MongoDB Atlas
    username = "casper"
    password = "caspero"
    cluster = "ClusterCrypto"
    client = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

    # Selecciona la base de datos que deseas utilizar
    db = client["CryptoData"]

    return db

db = get_mongo_db()

# set exchange
exchange = ccxt.binance({'enableRateLimit':True,'options': {'defaultType': 'future',},})

# set variables
now = exchange.milliseconds()
msec = 1000
minute = 60 * msec
hour = 60 * minute
limit = 1000
fromtime = ('2015-01-01 00:00:00')

# Funcion para obteber datos e insertarlos en la db
def save_candles(symbol, timeframe):

    # set varibles
    candles = []
    select_col = (symbol+"_"+timeframe)
    collection = db[select_col]
    from_timestamp = exchange.parse8601(fromtime)

    # Comprobamos si hay datos en db y eliminamos el ultimo registro
    try:
        last_data = pd.DataFrame(list(collection.find(sort=[("datetime", DESCENDING)]).limit(1)))
        from_timestamp = int(last_data['timestamp'].iloc[0])
        collection.delete_many({"timestamp":from_timestamp}) 
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde "+ str(last_data.iloc[0]["datetime"]))

    # Si no hay registros actualizamos desde el inicio
    except:
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde el inicio")
        collection = db.create_collection(select_col, index=[("datetime", DESCENDING)])

    # Iniciamos bucle de recolección hasta la fecha actual
    while(from_timestamp < now):

        # Intentamos descargas datos
        try:
            candles = exchange.fetch_ohlcv(symbol=symbol, timeframe=timeframe, limit=limit, since=from_timestamp)
            header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            df = pd.DataFrame(candles, columns=header)
            df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df.sort_values(by='timestamp', ascending=True)
            st.success("Descargado bloque de datos para "+ symbol+" en "+timeframe)

        # Sino hay datos, mostramos error
        except:
            st.error("Error actualizando datos de "+ symbol+" en "+timeframe)
            pass

        # Comprobamos si el bloque descargado tiene datos y los insertamos en db
        if len(candles) > 0:
            from_timestamp = int(df['timestamp'].iloc[-1] + minute)
            result = collection.insert_many(df.to_dict('records'))
            result.inserted_ids
            st.success("Insertado bloque de datos en base de datos de "+ symbol+" en "+timeframe)

        # Si no hay datos mostramos mensaje de bloque vacio
        else:
            st.error("Bloque vacio para "+symbol+" en "+timeframe + "desde"+ str(from_timestamp))