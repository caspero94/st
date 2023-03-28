# Resources
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import datetime
from functions import save_candles, get_mongo_db
import time

#setting config pagina streamlit
page_title = "Gráfico"
page_icon = ":chart:"
layout = "wide"
st.set_page_config( layout=layout,page_title=page_title, page_icon=page_icon)
#st.title(page_icon + " " + page_title)
st.markdown("""
        <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 3rem;
                }
                button[title="View fullscreen"] {
                    visibility: hidden;
                }
        </style>
        """, unsafe_allow_html=True)

#st.markdown("# Graficos")
#st.sidebar.markdown("# Graficos")

# Creamos diccionario de temporalidad y dias que se van a mostrar para esa temp.
timeframe_dict = {
"1m": ("1 Minuto", 12),
"3m": ("3 Minutos", 4),
"5m": ("5 Minutos", 8),
"15m": ("15 Minutos", 24),
"30m": ("30 Minutos", 48),
"1h": ("1 Hora", 96),
"2h": ("2 Horas", 192),
"4h": ("4 Horas", 384),
"6h": ("6 Horas", 576),
"8h": ("8 Horas", 768),
"12h": ("12 Horas", 1152),
"1d": ("1 Dia", 2304),
"3d": ("3 Dias", 6912),
"1w": ("1 Semana", 16128),
"1M": ("1 Mes", 69120),
}

timeframe_options = [timeframe_dict[key][0] for key in timeframe_dict]
timeframe_values = [key for key in timeframe_dict]

with st.sidebar:

    par = st.selectbox("Coin", ("BTC/BUSD","ETH/BUSD","BNB/BUSD"), label_visibility="collapsed")

    timeframe = st.selectbox("Coin", timeframe_values, format_func=lambda x: timeframe_dict[x][0], label_visibility="collapsed")
    timeframe_value = timeframe_dict[timeframe][1]

    date1, date2 = st.columns(2)
    with date1:
        fromdate = st.date_input("From:", datetime.date.today() - datetime.timedelta(hours=timeframe_value),label_visibility="collapsed")
        from_datetime = datetime.datetime.combine(fromdate, datetime.datetime.now().time())
    with date2:
        todate = st.date_input("To date:", datetime.date.today(),label_visibility="collapsed")
        to_datetime = datetime.datetime.combine(todate, datetime.datetime.max.time())

    with st.empty():
            if st.button('Actualizar datos', use_container_width=True):
                save_candles(symbol = par, timeframe = timeframe)

# Conecta a la base de datos
db = get_mongo_db()

# Selecciona la colección que deseas utilizar
select_col = (par+"_"+timeframe)
collection = db[select_col]

# Realiza una consulta a la colección filtrada por fechas
data_activo = pd.DataFrame(list(collection.find({'_id': {'$gte': from_datetime, '$lte': to_datetime}})))

# Comprobamos que data_activo contiene datos para plot y sino enviamos mensaje error
if (len(data_activo)) > 0:
        
    #data_activo = data_activo.set_index('datetime')
    with st.container():
        
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data_activo["_id"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
        #fig.add_trace(go.Histogram(x=data_activo[7]))
        fig.update_layout(#xaxis_title='Tiempo',
                #xaxis_title='Tiempo',
                #xaxis={'side': 'top'},
                #yaxis_title='Precio',
                yaxis={'side': 'right'},
                height = 800,
                margin=dict(l=0, r=0, t=0, b=0,pad=0),
                xaxis_rangeslider_visible=False)
        #fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
        #fig.update_xaxes(automargin='left+right')
        #'modeBarButtonsToAdd':['drawline','drawopenpath','drawcircle','drawrect','eraseshape',]
        configs = dict({'scrollZoom': False,'displaylogo': False} )
        st.plotly_chart(fig,use_container_width=True,config=configs)


        '''while True:
            time.sleep(15)
            #save_candles(symbol = par, timeframe = timeframe)
            update_time= datetime.datetime.now() - datetime.timedelta(minutes=2)
            update_now = datetime.datetime.now()
            data_activo_update = pd.DataFrame(list(collection.find({'_id': {'$gte': update_time, '$lte': update_now}})))
            data_activo = data_activo.append(data_activo_update)
            data_activo = data_activo.drop_duplicates(subset=['_id'])
            fig.update_traces(go.Candlestick(x=data_activo["_id"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))'''
                                    
else:
    st.info("No se encontraron datos disponibles para este activo y fechas")
