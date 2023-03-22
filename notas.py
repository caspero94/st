'''
     @st.cache_resource
     def init_connection():
          return MongoClient("mongodb+srv://st.secrets.db_username:st.secrets.db_pswd@st.secrets.cluster_name.6ydpkxh.mongodb.net/?retryWrites=true&w=majority")
     client = init_connection()


     @st.cache_data(ttl=600)
     def get_data():
          
          db = client.CryptoData
          collection = ["BTC/BUSD_1m"]
          items = db.collection.find().limit(10)
          items = list(items)
          return items

     items = get_data()
     st.write(items)

     fig = go.Figure()

     fig.add_trace(go.Candlestick(x=data_activo["datetime"], open=data_activo["open"], high=data_activo["high"], low=data_activo["low"], close=data_activo["close"]))
     #fig.add_trace(go.Histogram(x=data_activo["volume"]))
     fig.update_layout(
            #xaxis_title='Tiempo',
            #yaxis_title='Precio',

            height = 750,
            margin=dict(l=0, r=0, t=0, b=0,pad=0),
            xaxis_rangeslider_visible=False)
     fig.update_yaxes(automargin='left+top+right',ticklabelposition="inside")
     #fig.update_xaxes(automargin='left+right')
     configs = dict({'modeBarButtonsToAdd':['drawline',
                                    'drawopenpath',
                                    'drawcircle',
                                    'drawrect',
                                    'eraseshape',
                                ],'scrollZoom': True})
     st.plotly_chart(fig,use_container_width=True,config=configs)
    

    if selected == "Inicio":
        st.write("Iniciooo")
    
    if selected == "Graficos":
        switch_page("Graficos")


    if selected == "Obtener datos":
        switch_page("Graficos")

def menu_principal():

    return switch_page(selected)

with col4:
    timeframe_options = {
        "1m" : "1 Minuto",
        "3m" : "3 Minutos",
        }
    timeframe = st.selectbox(
        "Coin",
        ("1m","3m"),
        format_func = lambda x: timeframe_options.get(x),
        label_visibility="collapsed")
'''