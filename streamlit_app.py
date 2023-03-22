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

def get_mongo_db():
    # Configura tu conexión a la base de datos de MongoDB Atlas
    username = "casper"
    password = "caspero"
    cluster = "ClusterCrypto"
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")

    # Selecciona la base de datos que deseas utilizar
    db = client["CryptoData"]

    return db

# Conecta a la base de datos
db = get_mongo_db()

# Selecciona la colección que deseas utilizar
collection = db["BTC/BUSD_1m"]

# Realiza una consulta a la colección
df = pd.DataFrame(list(collection.find().limit(100)))
df.drop(['_id','timestamp'], axis=1, inplace=True)
df = df.set_index('datetime')
# Muestra el resultado en tu aplicación de Streamlit
st.write(df)



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