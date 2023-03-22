# Resources
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
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
    switch_page("Graficos")

if selected == "Graficos":
    switch_page("Graficos")


if selected == "Obtener datos":
    switch_page("Graficos")
