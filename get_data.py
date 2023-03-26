# Resources

import streamlit as st
import ccxt
from datetime import datetime
import pandas as pd
import dbmongo
import pymongo
# Conecta a la base de datos
db = dbmongo.get_mongo_db()


# set exchange
exchange = ccxt.binance({
    'enableRateLimit':True,
    'options': {
        'defaultType': 'future',
        },
})
# set variables
now = exchange.milliseconds()
msec = 1000
minute = 60 * msec
hour = 60 * minute
limit = 1000
fromtime = ('2015-01-01 00:00:00')

def save_candles(symbol, timeframe):
    candles = []
    select_col = (symbol+"_"+timeframe)
    collection = db[select_col]
    from_timestamp = exchange.parse8601(fromtime)
    try:
        last_data = pd.DataFrame(list(collection.find(sort=[("_id", pymongo.DESCENDING)]).limit(1)))
        from_timestamp = int(last_data['_id'].iloc[0])
        collection.delete_many({"_id":from_timestamp}) 
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde "+ str(last_data.iloc[0]["datetime"]))
        

    except:
        st.info("Actualizando "+ symbol+" en "+timeframe+" desde el incio")
        pass    
    while(from_timestamp < now):
        #try:
        '''candles = exchange.fetch_ohlcv(
        symbol = symbol,
        timeframe = timeframe,
        limit = limit,
        since = from_timestamp,
        )'''
        header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        df = pd.DataFrame(candles, columns = header)
        st.write(df)
        #df.insert(1, 'datetime', [datetime.fromtimestamp(d/1000) for d in df.timestamp])
        #df.insert(1, '_id', df["timestamp"])
        #st.write("Descargado bloque de datos para "+ symbol+" en "+timeframe)
        candles = df.sort_values(by='timestamp', ascending = True)
            
        #except:    
            #st.error("Error actualizando datos de "+ symbol+" en "+timeframe)
        #    pass
             
        
        if (len(candles)) > 0:
            from_timestamp = int(candles['_id'].iloc[-1] + minute)
            result = collection.insert_many(candles.to_dict('records'))
            result.inserted_ids
            #st.write("Insertado bloque de datos en base de datos de "+ symbol+" en "+timeframe)
        else:
            #st.write("Bloque de datos vacios para "+symbol+" en "+timeframe + "desde"+ str(from_timestamp))
            from_timestamp += hour * 1000
            
    #st.success("Datos actualizados para "+ symbol+" en "+timeframe)