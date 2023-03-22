# Resources
import streamlit as st
import dbmongo
import pandas as pd
import plotly.graph_objects as go

#variables
page_title = "Graficos"
page_icon = ":graph-up:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
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

#st.markdown("# Graficos")
#st.sidebar.markdown("# Graficos")

# Conecta a la base de datos
db = dbmongo.get_mongo_db()

# Selecciona la colección que deseas utilizar
collection = db["BTC/BUSD_1m"]

# Realiza una consulta a la colección
data_activo = pd.DataFrame(list(collection.find().limit(100)))
data_activo.drop(['_id','timestamp'], axis=1, inplace=True)
#data_activo = data_activo.set_index('datetime')
# Muestra el resultado en tu aplicación de Streamlit
fig = go.Figure()

fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
#fig.add_trace(go.Histogram(x=data_activo[7]))
fig.update_layout(
    #xaxis_title='Tiempo',
    #yaxis_title='Precio',

    #height = 750,
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