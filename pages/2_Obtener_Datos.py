# Resources
import streamlit as st
from menu import menu_p
#variables
page_title = "Obtener datos"
page_icon = ":file-bar-graph-fill:"
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

#st.markdown("# Obtener datos")
#st.sidebar.markdown("# Obtener datos")

def print_menu():
    menu_p()