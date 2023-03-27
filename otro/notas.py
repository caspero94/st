'''
     @st.cache_resource
     def init_connection():
          return MongoClient("mongodb+srv://st.secrets.db_username:st.secrets.db_pswd@st.secrets.cluster_name.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")
     client = init_connection()


     @st.cache_data(ttl=600)
     def get_data():
          
          db = client.CryptoData
          collection = ["BTC/BUSD_1m"]
          items = db.collection.find().limit(10)
          items = list(items)
          return items

     items = get_data()
     st.write(items)

     fig = go.Figure()

     fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
     #fig.add_trace(go.Histogram(x=data_activo["volume"]))
     fig.update_layout(
            #xaxis_title='Tiempo',
            #yaxis_title='Precio',

            height = 750,
            margin=dict(l=0, r=0, t=0, b=0,pad=0),
            xaxis_rangeslider_visible=False)
     fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
     #fig.update_xaxes(automargin='left+right')
     configs = dict({'modeBarButtonsToAdd':['drawline',
                                    'drawopenpath',
                                    'drawcircle',
                                    'drawrect',
                                    'eraseshape',
                                ],'scrollZoom': True})
     st.plotly_chart(fig,use_container_width=True,config=configs)
    

    if selected == "Inicio":
        st.write("Iniciooo")
    
    if selected == "Graficos":
        switch_page("Graficos")


    if selected == "Obtener datos":
        switch_page("Graficos")

def menu_principal():

    return switch_page(selected)

with col4:
    timeframe_options = {
        "1m" : "1 Minuto",
        "3m" : "3 Minutos",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m"),
        format_func = lambda x: timeframe_options.get(x),
        label_visibility="collapsed")

timeframe ="1m"
    m1, m3, m5, m15, m30, h1, h2, h4, h6, h8, h12, d1, d3, s1, me1 = st.columns(15, gap="small")
    with m1:
        if st.button('1m '):
            timeframe = "1m"
    with m3:
        if st.button('3m '):
            timeframe = "3m"
    with m5:
        if st.button('5m '):
            timeframe = "5m"
    with m15:
        if st.button('15m'):
            timeframe = "15m"
    with m30:
        if st.button('30m'):
            timeframe = "30m"
    with h1:
        if st.button('1h '):
            timeframe = "1h"
    with h2:
        if st.button('2h '):
            timeframe = "2h" 
    with h4:
        if st.button('4h '):
            timeframe = "4h"    
    with h6:
        if st.button('6h '):
            timeframe = "6h" 
    with h8:
        if st.button('8h '):
            timeframe = "8h" 
    with h12:
        if st.button('12h'):
            timeframe = "12h" 
    with d1:
        if st.button('1D '):
            timeframe = "1d" 
    with d3:
        if st.button('3D '):
            timeframe = "3d" 
    with s1:
        if st.button('1S '):
            timeframe = "1S" 
    with me1:
        if st.button('1M '):
            timeframe = "1M"   
---------------------------
# menu.py

# Resources
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
# Horizontal menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Inicio","Graficos","Obtener datos"], 
        icons=["house","graph-up","file-bar-graph-fill"], menu_icon="cast", default_index=1)
    selected
    
if selected == "Inicio":
    pass
if selected == "Graficos":
    switch_page("Graficos")

if selected == "Obtener datos":
    switch_page("Obtener datos")

--------------------------------
# page_config.py

# Resources
import streamlit as st

#variables
page_title = "Proyect X"
page_icon = ":graph-up:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_icon + " " + page_title)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

'''