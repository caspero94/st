# Resources
import dbmongo
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

#variables
page_title = "Graficos"
page_icon = ":chart:"
layout = "wide"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout,)
st.title(page_icon + " " + page_title)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 2rem;
                    padding-left: 2rem;
                    padding-right: 4rem;
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
col1, col2 = st.columns(2)
with col1:
    par = st.selectbox(
        "Coin",
        ("BTC/BUSD","BNB/BUSD"),label_visibility="collapsed")

with col2:
    timeframe_options = {
        "1m" : "1 Minuto",
        "3m" : "3 Minutos",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m"),
        format_func = lambda x: timeframe_options.get(x),
        label_visibility="collapsed")


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
        xaxis_title='Tiempo',
        yaxis_title='Precio',

        height = 700,
        margin=dict(l=0, r=0, t=0, b=0,pad=0),
        xaxis_rangeslider_visible=False)
    #fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
    #fig.update_xaxes(automargin='left+right')
    #'modeBarButtonsToAdd':['drawline','drawopenpath','drawcircle','drawrect','eraseshape',]
    configs = dict({'scrollZoom': False,'displaylogo': False} )
    st.plotly_chart(fig,use_container_width=True,config=configs)