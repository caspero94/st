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
     st.write("Esta es la conexion a mongo db"+st.secrets["mg_connect"])
     client = init_connection()


if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")