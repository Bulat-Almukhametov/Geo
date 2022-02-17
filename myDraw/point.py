from PIL import Image, ImageDraw

import variables
import myDraw.pointFromGeo
import myDraw.colorFromSpei


def draw(geo, spei, image: Image.Image):
    x, y = myDraw.pointFromGeo.get(geo, image)

    shape = [
        x - variables.RECT_WIDTH,
        y - variables.RECT_HEIGHT,
        x + variables.RECT_WIDTH,
        y + variables.RECT_HEIGHT,
    ]

    r, g, b = myDraw.colorFromSpei.get(spei)

    draw = ImageDraw.Draw(image)
    draw.rectangle(shape, fill=(r, g, b, variables.RECT_OPACITY))
