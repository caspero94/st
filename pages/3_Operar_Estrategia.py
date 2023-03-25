# Resources
import streamlit as st

#variables
page_title = "Test Estragia"
page_icon = ":bar_chart:"
layout = "wide"

#setting title for our app
st.set_page_config( layout=layout,page_title=page_title, page_icon=page_icon)
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