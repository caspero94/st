import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objects as go
import dbmongo

#variables
page_title = "Proyect X"
page_icon = ":money_with_wings:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")



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
    # Conecta a la base de datos
    db = dbmongo.get_mongo_db()

    # Selecciona la colección que deseas utilizar
    collection = db["BTC/BUSD_1m"]

    # Realiza una consulta a la colección
    data_activo = pd.DataFrame(list(collection.find().limit(1000)))
    data_activo.drop(['_id','timestamp'], axis=1, inplace=True)
    #data_activo = data_activo.set_index('datetime')
    # Muestra el resultado en tu aplicación de Streamlit
    fig = go.Figure()

    fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
    #fig.add_trace(go.Histogram(x=data_activo[7]))
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

if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")