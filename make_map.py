import folium
m = folium.Map(
    location=[1.3521, 103.8198],
    zoom_start=11,
    tiles="cartodbpositron"
)
folium.Marker(
    [1.3521, 103.8198],
    popup="Singapore",
).add_to(m)
m.save("map.html")