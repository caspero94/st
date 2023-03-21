import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu

with st.sidebar:
     selected = option_menu(
          menu_title="Menu Principal",
          options=["Grafico","Obtener datos"],
          icons=["graph-up","database",],
          menu_icon="list",
          default_index=0
     )

# Horizontal menu

selected = option_menu(
          menu_title="Menu Principal",
          options=["Grafico","Obtener datos"],
          icons=["graph-up","database",],
          menu_icon="list",
          default_index=0,
          orientation="horizontal",
     )


if selected == "Grafico":
     st.title(f"Selecionado {selected}")
if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")