# Resources
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

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

st.write("INICIO")

#st.markdown("# Inicio")
#st.sidebar.markdown("# Inicio")



