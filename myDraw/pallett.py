from PIL import Image, ImageDraw

import variables

def draw_pallett(image: Image.Image):
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, 0, variables.PALLETTE_WIDTH, variables.PALLETTE_HEIGHT], fill='red')
