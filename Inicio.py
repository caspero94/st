# Resources
import page_config
from menu import menu_p
import streamlit as st


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

def print_menu():
    menu_p()


print_menu()

