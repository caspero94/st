# Resources Global
import pymongo

# Función para obtener base datos mongo
def get_mongo_db():

    # Configura tu conexión a la base de datos de MongoDB Atlas
    username = "casper"
    password = "caspero"
    cluster = "ClusterCrypto"
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

    # Selecciona la base de datos que deseas utilizar
    db = client["CryptoData"]

    return db

##################################

# Funcion para obtener datos e insertarlos en la db
def save_candles(symbol, timeframe):

    # Resources
    import ccxt
    import pandas as pd
    import streamlit as st
    from datetime import datetime

    # Conecta a la base de datos y set collection
    db = get_mongo_db()
    select_col = (symbol+"_"+timeframe)
    collection = db[select_col]

    # set exchange
    exchange = ccxt.binance({'enableRateLimit':True,'options': {'defaultType': 'future',},})

    # set variables
    now = exchange.milliseconds()
    msec = 1000
    minute = 60 * msec
    hour = 60 * minute
    limit = 1000
    fromtime = ('2015-01-01 00:00:00')
    candles = []
    from_timestamp = exchange.parse8601(fromtime)

    # Comprobamos si hay datos previos, si hay, eliminamos el ultimo registro para actualizarlo y sino hay empezamos desde el inicio
    try:
        last_data = pd.DataFrame(list(collection.find_one(sort=[("_id", pymongo.DESCENDING)])))
        from_timestamp = int(last_data['timestamp'].iloc[0])
        collection.delete_one({"timestamp":from_timestamp}) 
        st.info("Actualizando "+ symbol+"-"+timeframe+" desde "+ str(last_data.iloc[0]["_id"]))
        
    except:
        st.info("Actualizando "+ symbol+"-"+timeframe+" desde el incio")
        pass    

    # Iniciamos buble recolección de datos hasta llegar a la fecha de hoy
    while(from_timestamp < now):
        try:
            # Descargamos del exchange los OHLCV
            candles = exchange.fetch_ohlcv(symbol = symbol,timeframe = timeframe,limit = limit,since = from_timestamp,)
            header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            df = pd.DataFrame(candles, columns = header)
            
            # Agregamos la fecha de la vela como ID y ordenamos tabla
            df.insert(1, '_id', [datetime.fromtimestamp(d/1000) for d in df.timestamp])
            candles = df.sort_values(by='_id', ascending = True)

            # Mensaje completado try
            st.info("Descargado datos para "+ symbol+"-"+timeframe)
            
        # Mostramos error en caso de no haber podido completar la descarga OHLCV    
        except:    
            st.error("Error actualizando datos de "+ symbol+"-"+timeframe)
            pass
             
        # Comprobamos que candles contiene información
        if (len(candles)) > 0:
            # Actualizamos variable de from_timestamp para la siguiente busqueda
            from_timestamp = int(df['timestamp'].iloc[-1] + minute)
            result = collection.insert_many(df.to_dict('records'))
            result.inserted_ids
            #st.write("Insertado bloque de datos en base de datos de "+ symbol+" en "+timeframe)
        else:
            # Actualizamos variable de from_timestamp para la siguiente busqueda ya que no hay datos
            st.error("Bloque de datos vacios para "+symbol+"-"+timeframe + " - "+ str(from_timestamp))
            from_timestamp += hour * 1000

    # Proceso finalizado        
    st.success("Datos actualizados para "+ symbol+"-"+timeframe)