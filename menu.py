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
