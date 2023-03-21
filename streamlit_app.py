import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu

with st.sidebar:
     selected = option_menu(
          menu_title="Menu Principal",
          options=["Graficos","Obtener datos"],
          icons=["graph-up","database",],
          menu_icon="list",
          default_index=0
     )


if selected == "Graficos":
     st.title(f"Selecionado {selected}")
if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")