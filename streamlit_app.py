import streamlit as st
from streamlit_option_menu import option_menu
from pymongo import MongoClient
import pandas as pd
import plotly.graph_objects as go

# Horizontal menu
selected = option_menu(
          menu_title=None,
          options=["Grafico","Obtener datos"],
          icons=["graph-up","file-bar-graph-fill"],
          menu_icon="list",
          default_index=0,
          orientation="horizontal",
          styles={
                "container": {"padding": "0!important", "background-color": "#363636"},
                "icon": {"color": "white", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#8a0000",
                },
                "nav-link-selected": {"background-color": "#470000"},
            },
     )


if selected == "Grafico":

     st.title(f"Selecionado {selected}")
     @st.cache_resource
     def init_connection():
          return MongoClient(st.secrets["mg_connect"])
     st.write("Esta es la conexion a mongo db"+st.secrets["mg_connect"]+"dee"+st.secrets["mg_connect2"])
     client = init_connection()

'''
     @st.cache_data(ttl=600)
     def get_data():
          db = client["CryptoData"]
          collection = db["BTC/BUSD_1m"]
          items = pd.DataFrame(list(collection.find().limit(100)))
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
     st.plotly_chart(fig,use_container_width=True,config=configs)'''
if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")