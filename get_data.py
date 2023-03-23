# Resources
from dbmongo import get_mongo_db
import streamlit as st
import ccxt
from datetime import datetime
import pandas as pd

# Conecta a la base de datos
db = get_mongo_db()
st.write(db)
# set exchange
exchange = ccxt.binance({
    'enableRateLimit':True,
    'options': {
        'defaultType': 'future',
        },
})
st.write(exchange)
# set variables
now = exchange.milliseconds()
msec = 1000
minute = 60 * msec
hour = 60 * minute
limit = 1000
fromtime = ('2015-01-01 00:00:00')

def save_candles(symbol, timeframe):
    collection = db[symbol+"_"+timeframe]
    from_timestamp = exchange.parse8601(fromtime)
    st.write("Iniciando recoleccion de datos de "+ symbol+" en "+timeframe)
    try:
        last_data = pd.DataFrame(list(collection.find(sort=[("timestamp", pymongo.DESCENDING)]).limit(1)))
        from_timestamp = int(last_data['_id'].iloc[0])
        st.write(from_timestamp)
        collection.delete_many({"_id":from_timestamp}) 
        st.write("Datos previos encontrados, actualizando desde "+ str(last_data.iloc[0]["datetime"]))
        

    except:
        st.write("No hay datos previos, recolectando desde el inicio")
        pass    
    while(from_timestamp < now):
        try:
            candles = exchange.fetch_ohlcv(
            symbol = symbol,
            timeframe = timeframe,
            limit = limit,
            since = from_timestamp,
            )
            
            header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            df = pd.DataFrame(candles, columns = header)
            df.insert(1, 'datetime', [datetime.fromtimestamp(d/1000) for d in df.timestamp])
            df.insert(1, '_id', df["timestamp"])
            st.write("Downloading data collection from "+ symbol+" in "+timeframe)
            candles = df.sort_values(by='timestamp', ascending = False)
            
        except:
            st.write("Error descargando datos de "+ symbol+" en "+timeframe)
            pass
             
        
        if 'candles' in locals() and len(candles) > 0:
            st.write("if candles > 0")
            from_timestamp = int(candles['timestamp'].iloc[0] + minute)
            st.write("obtenemos from_timestamp y le sumamos 1 minuto")
            result = collection.insert_many(candles.to_dict('records'))
            result.inserted_ids
            st.write("Insertado bloque de datos en base de datos de "+ symbol+" en "+timeframe)
        else:
            st.write("Bloque de datos vacios para "+symbol+" en "+timeframe + "desde"+ from_timestamp)
            from_timestamp += hour * 1000
            
    st.write("Completado obtención de datos para "+ symbol+" en "+timeframe)