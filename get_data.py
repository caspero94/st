# Resources
import streamlit as st
import ccxt
from datetime import datetime
import pandas as pd
import dbmongo
import pymongo
from pymongo import ASCENDING
# Conecta a la base de datos
db = dbmongo.get_mongo_db()

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
        last_data = pd.DataFrame(list(collection.find(sort=[("_id", pymongo.DESCENDING)]).limit(1)))
        from_timestamp = int(last_data['timestamp'].iloc[0])
        collection.delete_many({"timestamp":from_timestamp}) 
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde "+ str(last_data.iloc[0]["_id"]))
        
    # Si no hay registros actualizamos desde el inicio
    except:
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde el incio")
        collection.create_index([("_id", ASCENDING)], name="datetime", unique=True)
        pass    
    
    # Iniciamos buble de recolección hasta la fecha actual     
    while(from_timestamp < now):

        # Intentamos descargas datos
        try:
            candles = exchange.fetch_ohlcv(symbol = symbol,timeframe = timeframe,limit = limit,since = from_timestamp,)
            header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            df = pd.DataFrame(candles, columns = header)
            df.insert(1, 'datetime', [datetime.fromtimestamp(d/1000) for d in timestamp._id])
            df = df.sort_values(by='_id', ascending = True)
            st.success("Descargado bloque de datos para "+ symbol+" en "+timeframe)

        # Sino hay datos, mostramos error    
        except:    
            st.error("Error actualizando datos de "+ symbol+" en "+timeframe)
            pass
             
        # Comprobamos si el bloque descargado tiene datos y los insertamos en db
        if (len(candles)) > 0:
            from_timestamp = int(df['timestamp'].iloc[-1] + minute)
            result = collection.insert_many(df.to_dict('records'))
            result.inserted_ids
            st.success("Insertado bloque de datos en base de datos de "+ symbol+" en "+timeframe)

        # Si no hay datos mostramos mensaje de bloque vacio    
        else:
            st.error("Bloque vacio para "+symbol+" en "+timeframe + "desde"+ str(from_timestamp))
            from_timestamp += hour * 1000
    
    # Terminamos el bucle y mostramos mensaje de completado        
    st.success("Datos actualizados para "+ symbol+" en "+timeframe)