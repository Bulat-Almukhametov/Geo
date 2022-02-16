from PIL import Image

import variables

map_width = variables.OST_COORD - variables.WEST_COORD
map_height = variables.NORD_COORD - variables.SOUTH_COORD

def get(geo, image: Image.Image):
    lat, long = geo

    x = (long - variables.WEST_COORD) / map_width * image.width
    y = (variables.NORD_COORD - lat) / map_height * image.height

    return (x, y)
