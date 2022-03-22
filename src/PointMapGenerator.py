import folium 
import io
from PIL import Image

class PointMapGenerator:
    def generateMap(this, center, points):
        
        pathToImage = './img/map.png'
        newMap = folium.Map(location = center, zoom_start = 16)

        folium.Marker(
            location = center,
            icon = folium.DivIcon(html=f""" <div style = 'height: 30px; width:30px; border-radius: 50%; background-color: red'></div>""")
        ).add_to(newMap)

        for point in points:
            folium.Marker(
                location = point,
            ).add_to(newMap)

        img_data = newMap._to_png(1)
        img = Image.open(io.BytesIO(img_data))
        img.save(pathToImage)
        return pathToImage

       