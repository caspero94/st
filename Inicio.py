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

#st.markdown("# Inicio")
#st.sidebar.markdown("# Inicio")
    


# Horizontal menu
selected = option_menu(
          menu_title=None,
          options=["Inicio","Graficos","Obtener datos"],
          icons=["house","graph-up","file-bar-graph-fill"],
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
if selected == "Inicio":
    switch_page("Inicio")
    st.title(f"Selecionado {selected}")
if selected == "Graficos":
    switch_page("Graficos")
    st.title(f"Selecionado {selected}")

if selected == "Obtener datos":
    switch_page("Graficos")
    st.title(f"Selecionado {selected}")


