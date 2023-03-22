import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objects as go
import pymongo

#variables
page_title = "Proyect X"
page_icon = ":money_with_wings:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://"**st.secrets["mongo"])

client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client.CryptoData
    collection = db["BTC/BUSD_1m"]
    items = collection.find().limit(2)
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

for item in items:
    st.write(f"{item['datetime']} has a :{item['close']}:")


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
     st.header("Grafico")


if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")