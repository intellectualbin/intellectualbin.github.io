import folium
import pandas as pd
# A small table of places — think of this as rows in a spreadsheet
data = {
    "name": ["Marina Bay Sands", "Gardens by the Bay", "Sentosa", "Changi Airport"],
    "lat": [1.2834, 1.2816, 1.2494, 1.3644],
    "lon": [103.8607, 103.8636, 103.8303, 103.9915],
}
df = pd.DataFrame(data)

# Center the map on Singapore, same as before
m = folium.Map(
    location=[1.3521, 103.8198],
    zoom_start=11,
    tiles="cartodbpositron",
)

# Loop through every row of the DataFrame and add a marker for it
for index, row in df.iterrows():
    folium.Marker(
        [row["lat"], row["lon"]],
        popup=row["name"],
    ).add_to(m)

m.save("map.html")