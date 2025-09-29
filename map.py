import folium


rutas =  [(-40.0877,-72.5189),
       (-37.46973,-72.35366)]

ruta1=[(-40.0877,-72.5189),
       (-40.283333,-72.05)]

ruta2=[(-40.0877,-72.5189),
       (-40,-72)]

ruta3=[(-40.0877,-72.5189),   
       (-40.2475,-72.385278)]

ruta4=[(-40.0877,-72.5189),   
       (-40.1978,-72.2598)]

ruta5=[(-40.0877,-72.5189),   
       (-40.133333,-72.4)]

ruta6=[(-37.46973,-72.35366),   
       (-36.82699, -73.04977)]

ruta7=[(-37.46973,-72.35366),   
       (-36.60664, -72.10344)]

ruta8=[(-37.46973,-72.353669),   
       (-37.666666666667, -72.016666666667)]

ruta9=[(-37.46973,-72.353669),   
       (-33.45694, -70.64827)]


ruta10=[(-37.46973,-72.353669),   
       (-33.02457, -71.55183)]

ruta11=[(-37.46973,-72.353669),   
       (-35.33321, -72.41156)]

ruta12=[(-37.46973,-72.353669),   
       (-36.72494, -73.11684)]

ruta13=[(-37.46973,-72.353669),   
       (-37.333333,  -71.683333)]

ruta14=[(-37.46973,-72.353669),
        (-37.215556,-72.383333)]

ruta15=[(-37.46973,-72.353669),
        (-39.81422, -73.24589)]

ruta16=[(-37.46973,-72.353669),
        (-37.79519 , -72.71636)]


        


mapa=folium.Map(location=[-37.46973,-72.35366],zoom_start=7)


####Marcadores

folium.Marker(location=(-36.72494, -73.11684),
              tooltip="Click",
              popup="Talcahuano"
              ).add_to(mapa)

folium.Marker(location=(-35.33321, -72.41156),
                tooltip="Click", 
                popup="Constitucion"
                ).add_to(mapa)

folium.Marker(location=(-33.45694, -70.64827),
              tooltip="Click", 
              popup="Santiago"
              ).add_to(mapa)

folium.Marker(location=(-33.02457, -71.55183),
                tooltip="Click",
                popup="Viña del mar"
                ).add_to(mapa)



folium.Marker(location=(-37.666666666667, -72.016666666667),
                tooltip="Click",
                popup="Santa barbara"
                ).add_to(mapa)

folium.Marker(
    location=(-40.0877,-72.5189),
    tooltip="Click",
    popup="Nontuela, Granny house",
    
).add_to(mapa)

folium.Marker(location=(-36.60664, -72.10344),
              tooltip="Click",
                popup="Chillan",
                ).add_to(mapa)


folium.Marker(location=(-36.82699, -73.04977),
                tooltip="Click",
                popup="Concepcion",
                ).add_to(mapa)

folium.Marker(location=(-37.46973,-72.35366),
              tooltip="Click",
              popup="Los Angeles",
              icon=folium.Icon(icon="home")).add_to(mapa)

folium.Marker(location=(-40.283333,-72.05),
              tooltip="click",
              popup="Lago maihue",
              ).add_to(mapa)

folium.Marker(location=(-40.2475,-72.385278),
              tooltip="click",
              popup="Lago Ranco",
                ).add_to(mapa)

folium.Marker(location=(-40,-72),
              tooltip="click",
              popup="Arquilhue",
                ).add_to(mapa)


folium.Marker(location=(-40.1978,-72.2598),
              tooltip="click",
              popup="Llifen",
                ).add_to(mapa)

folium.Marker(location=(-40.133333,-72.4),
              tooltip="click",
              popup="Futrono",
                ).add_to(mapa)

folium.Marker(location=(-37.215556,-72.383333),
              tooltip="click",
              popup="Salto del laja",
                ).add_to(mapa)

folium.Marker(location=(-39.81422, -73.24589),
                tooltip="click",
                popup="Valdivia",
                   ).add_to(mapa)

folium.Marker(location=(-37.333333,  -71.683333),
              tooltip="click",
                popup="Antuco",
                    ).add_to(mapa)


folium.Marker(location=(-37.79519 , -72.71636),
                tooltip="click",
                popup="Angol",
                   ).add_to(mapa)


              


###Lineas
folium.PolyLine(rutas, color="red", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta1, color="blue", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta3, color="green", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta2, color="yellow", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta4, color="purple", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta5, color="orange", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta6, color="black", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta7, color="brown", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta8, color="pink", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta9, color="gray", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta10, color="purple", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta11, color="blue", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta12, color="green", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta13, color="yellow", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta14, color="orange", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta15, color="black", weight=2.5, opacity=1).add_to(mapa)
folium.PolyLine(ruta16, color="black" , weight=2.5 , opacity=1).add_to(mapa)



mapa.save('map.html')
