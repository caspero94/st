# Resources
import dbmongo
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import datetime

#variables
page_title = "Graficos"
page_icon = ":chart:"
layout = "wide"
#page_title=page_title, page_icon=page_icon,
#setting title for our app
st.set_page_config( layout=layout,)
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

# Conecta a la base de datos
db = dbmongo.get_mongo_db()

# Menu coins
col1, col2, col3, col4, col5 = st.columns([1,1,2,2,2])
with col1:
    par = st.selectbox(
        "Coin",
        ("BTC/BUSD","ETH/BUSD","BNB/BUSD"),label_visibility="collapsed")

with col2:
    timeframe_options = {
        "1m" : "1 Minuto",
        "3m" : "3 Minutos",
        "5m" : "5 Minutos",
        "15m" : "15 Minutos",
        "30m" : "30 Minutos",
        "1h" : "1 Hora",
        "2h" : "2 Horas",
        "4h" : "4 Horas",
        "6h" : "6 Horas",
        "8h" : "8 Horas",
        "12h" : "12 Horas",
        "1d" : "1 Dia",
        "3d" : "3 Dias",
        "1w" : "1 Semana",
        "1M" : "1 Mes",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m","5m","15m","30m","1h","2h","4h","6h","8h","12h","1d","3d","1w","1M"),
        format_func = lambda x: timeframe_options.get(x), 
        label_visibility="collapsed")
with col3:
    timeframe_days = {
        "1m" : 0,
        "3m" : 1,
        "5m" : 2,
        "15m" : 5,
        "30m" : 7,
        "1h" : 14,
        "2h" : 30,
        "4h" : 60,
        "6h" : 80,
        "8h" : 100,
        "12h" : 120,
        "1d" : 240,
        "3d" : 360,
        "1w" : 720,
        "1M" : 1440,
        }
    st.write(timeframe)
    wdays = timeframe(lambda timeframe: timeframe_days.get(timeframe))
    st.write(wdays)
    date1, date2 = st.columns(2)
    with date1:
        fromdate = st.date_input(
            "From:",
            datetime.date.today() - datetime.timedelta(days=1),label_visibility="collapsed")
    with date2:
        todate = st.date_input(
            "To date:",
            datetime.date.today(),label_visibility="collapsed")

with col5:
    with st.empty():
        if st.button('Actualizar datos', use_container_width=True):
                from get_data import save_candles
                save_candles(
                symbol = par, 
                timeframe = timeframe,
                )
        
with col4:
    st.empty()




# Selecciona la colección que deseas utilizar
select_col = (par+"_"+timeframe)
collection = db[select_col]

# Formateamos fechas para consulta en base datos
from_datetime = datetime.datetime.combine(fromdate, datetime.datetime.min.time())
to_datetime = datetime.datetime.combine(todate, datetime.datetime.max.time())

# Realiza una consulta a la colección filtrada por fechas
data_activo = pd.DataFrame(list(collection.find({'datetime': {'$gte': from_datetime, '$lte': to_datetime}})))

# Comprobamos si data_activo contiene datos para plot y sino enviamos mensaje error
if (len(data_activo)) > 0:
        
    # Eliminamos columnas inecesarias
    data_activo.drop(['_id','timestamp'], axis=1, inplace=True)
    #data_activo = data_activo.set_index('datetime')
    with st.container():
        fig = go.Figure()

        fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
        #fig.add_trace(go.Histogram(x=data_activo[7]))
        fig.update_layout(
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
else:
    st.info("No se encontraron datos disponibles para este activo y fechas")
