import streamlit as st
st.title("Proyecto X")
menu = st.selectbox("Menu Principal",("Obtener datos", "Graficos"))
st.write("Has selecionado", menu)