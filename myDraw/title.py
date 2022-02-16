from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

import variables

def draw(title, image: Image.Image):
    try:
        title = datetime.strptime(title, '%Y-%m-%d').strftime('%b %Y')
    except:
        pass

    fnt = ImageFont.truetype(f'{variables.TITLE_FONT_NAME}.ttf', variables.TITLE_FONT_SIZE)
    txt_image = Image.new(
        "RGBA",
        image.size,
        (255, 255, 255, 0),
    )

    draw = ImageDraw.Draw(txt_image)
    draw.text(
        (variables.TITLE_POSITION_X, variables.TITLE_POSITION_Y),
        title,
        (
            variables.TITLE_FONT_COLOR_R,
            variables.TITLE_FONT_COLOR_G,
            variables.TITLE_FONT_COLOR_B,
            variables.TITLE_FONT_OPACITY,
        ),
        fnt,
    )

    return Image.alpha_composite(image, txt_image)