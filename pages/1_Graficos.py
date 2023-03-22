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

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout,)
st.title(page_icon + " " + page_title)
st.markdown("""
        <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
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

# Obtener collections
col1, col2, col3 = st.columns([1,5,1])
with col1:
    par = st.selectbox(
        "Coin",
        ("BTC/BUSD","BNB/BUSD"),label_visibility="collapsed")

with col2:
    m1, m3, m5, m15, m30, h1, h2, h4, h6, h8, h12, d1, d3, s1, me1 = st.columns(15, gap=small)
    with m1:
        if st.button('1m'):
            timeframe = "1m"
    with m3:
        if st.button('3m'):
            timeframe = "3m"
    with m5:
        if st.button('5m'):
            timeframe = "5m"
    with m15:
        if st.button('15m'):
            timeframe = "15m"
    with m30:
        if st.button('30m'):
            timeframe = "30m"
    with h1:
        if st.button('1h'):
            timeframe = "1h"
    with h2:
        if st.button('2h'):
            timeframe = "2h" 
    with h4:
        if st.button('4h'):
            timeframe = "4h"    
    with h6:
        if st.button('6h'):
            timeframe = "6h" 
    with h8:
        if st.button('8h'):
            timeframe = "8h" 
    with h12:
        if st.button('12h'):
            timeframe = "12h" 

with col3:
    date1, date2 = st.columns(2)
    with date1:
        fromdate = st.date_input(
            "From:",
            datetime.date.today() - datetime.timedelta(days=7),label_visibility="collapsed")
    with date2:
        todate = st.date_input(
            "To date:",
            datetime.date.today(),label_visibility="collapsed")
'''with col4:
    timeframe_options = {
        "1m" : "1 Minuto",
        "3m" : "3 Minutos",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m"),
        format_func = lambda x: timeframe_options.get(x),
        label_visibility="collapsed")
'''
# Selecciona la colección que deseas utilizar
select_col = (par+"_"+timeframe)
collection = db[select_col]

# Realiza una consulta a la colección
data_activo = pd.DataFrame(list(collection.find().limit(100)))
data_activo.drop(['_id','timestamp'], axis=1, inplace=True)
#data_activo = data_activo.set_index('datetime')
# Muestra el resultado en tu aplicación de Streamlit
with st.container():
    fig = go.Figure()

    fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
    #fig.add_trace(go.Histogram(x=data_activo[7]))
    fig.update_layout(
        #xaxis_title='Tiempo',
        #yaxis_title='Precio',

        #height = 700,
        margin=dict(l=0, r=0, t=0, b=0,pad=0),
        xaxis_rangeslider_visible=False)
    #fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
    #fig.update_xaxes(automargin='left+right')
    #'modeBarButtonsToAdd':['drawline','drawopenpath','drawcircle','drawrect','eraseshape',]
    configs = dict({'scrollZoom': False,'displaylogo': False} )
    st.plotly_chart(fig,use_container_width=True,config=configs)