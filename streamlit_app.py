import streamlit as st
from streamlit_option_menu import option_menu

# Horizontal menu
selected = option_menu(
          menu_title=None,
          options=["Grafico","Obtener datos"],
          icons=["graph-up","database",],
          menu_icon="list",
          default_index=0,
          orientation="horizontal",
          styles={
                "container": {"padding": "0!important", "background-color": "#000000"},
                "icon": {"color": "black", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "black"},
            },
     )


if selected == "Grafico":
     st.title(f"Selecionado {selected}")
if selected == "Obtener datos":
     st.title(f"Selecionado {selected}")