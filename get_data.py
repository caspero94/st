# Resources
import dbmongo
import streamlit as st
import ccxt
from datetime import datetime
import pandas as pd

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
    collection = db[symbol+"_"+timeframe]
    from_timestamp = exchange.parse8601(fromtime)
    st.write("Starting data collection from "+ symbol+" in "+timeframe)
    try:
        last_data = pd.DataFrame(list(collection.find(sort=[("timestamp", pymongo.DESCENDING)]).limit(1)))
        from_timestamp = int(last_data['_id'].iloc[0])
        collection.delete_many({"_id":from_timestamp}) 
        st.write("Previous data found, updating from "+ str(last_data.iloc[0]["datetime"]))
        

    except:
        st.write("No previous data, getting from start")
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
            st.write("Error Downloading data collection from "+ symbol+" in "+timeframe)
            pass
             
        
        if (len(candles)) > 0:
            from_timestamp = int(candles['timestamp'].iloc[0] + minute)
            result = collection.insert_many(candles.to_dict('records'))
            result.inserted_ids
            st.write("Insert data in db of collection from "+ symbol+" in "+timeframe)
        else:
            st.write("Empty data "+symbol+"_"+timeframe)
            from_timestamp += hour * 1000
            
    st.write("Complete data collection from "+ symbol+" in "+timeframe)