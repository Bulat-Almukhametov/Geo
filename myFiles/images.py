from PIL import Image
from typing import Sequence

import variables

def getMapTemplate():
    return Image.open(variables.MAP_SRC)

def save(file, image: Image.Image):
    image.save(f'{variables.TARGET_FOLDER}/{file}.png')

def saveAnimation(images: Sequence[Image.Image]):
    images[0].save(
        variables.ANIMATION_NAME,
        save_all=True,
        append_images=images[1:],
        duration=variables.FRAME_DURATION,
        loop=0,
    )