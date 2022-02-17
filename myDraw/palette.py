from PIL import Image, ImageDraw, ImageFont
import myDraw.colorFromSpei

import variables

def draw(image: Image.Image):
    draw = ImageDraw.Draw(image)
    spei_range = variables.SPEI_TO - variables.SPEI_FROM
    prev_spei = variables.SPEI_FROM
    prev_Y = variables.PALETTE_POSITION_Y

    for i in range(variables.PALETTE_COLORS_COUNT):
        fill_percent = (i + 1) / variables.PALETTE_COLORS_COUNT
        shape = [
                variables.PALETTE_POSITION_X,
                prev_Y,
                variables.PALETTE_POSITION_X + variables.PALETTE_WIDTH,
                variables.PALETTE_POSITION_Y + fill_percent * variables.PALETTE_HEIGHT,
            ]
        spei = round(variables.SPEI_FROM + fill_percent * spei_range, 2)


        draw.rectangle(shape, fill=myDraw.colorFromSpei.get(spei))

        draw.text(
            (shape[2] + variables.PALETTE_TEXT_MARGIN, shape[3] - variables.PALETTE_FONT_SIZE),
            f'from {prev_spei} to {spei}',
            (
                variables.PALETTE_FONT_COLOR_R,
                variables.PALETTE_FONT_COLOR_G,
                variables.PALETTE_FONT_COLOR_B,
            ),
            ImageFont.truetype(f'{variables.PALETTE_FONT_NAME}.ttf', variables.PALETTE_FONT_SIZE),
        )

        prev_spei = spei
        prev_Y = shape[3]
    


    return image
