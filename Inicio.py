# Resources
import streamlit as st

#variables
page_title = "Proyect X"
page_icon = ":coin:"
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

st.header("Proyecto en desarrollo")
st.write("Objetivos:")
st.write("1: Plataforma para visualizar datos de activos")
st.write("2: Plataforma para obtener datos actualizados de activos")
st.write("3: Plataforma para testear estrategias con los datos de activos")
st.write("4: Plataforma para operar estrategias y visualizar resultados de las mismas")