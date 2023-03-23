# Resources
import streamlit as st

#variables
page_title = "Obtener Datos"
page_icon = ":bar_chart:"
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
                    padding-right: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)

#st.markdown("# Obtener datos")
#st.sidebar.markdown("# Obtener datos")

st.write("OBTENER DATOS")
col1, col2, col3, col4 = st.columns([1,1,2,7])
with col1:
    par = st.selectbox(
        "Coin",
        ("BTC/BUSD","BNB/BUSD"),label_visibility="collapsed")

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
        "1D" : "1 Dia",
        "3D" : "3 Dias",
        "1S" : "1 Semana",
        "1M" : "1 Mes",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m","5m","15m","30m","1h","2h","4h","6h","8h","12h","1D","3D","1S","1M"),
        format_func = lambda x: timeframe_options.get(x),
        label_visibility="collapsed")