# Resources
import streamlit as st

#variables
page_title = "Proyect X"
page_icon = ":graph-up:"
layout = "centered"

#setting title for our app
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_icon + " " + page_title)