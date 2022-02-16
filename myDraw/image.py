from PIL import Image

import myDraw.point

def drawPointsLayer(template_image: Image.Image, points):
    target_image = template_image.copy()
    overlay = Image.new('RGBA', target_image.size, (0, 0, 0, 0))
    
    for geo_coords, spei in points:
        myDraw.point.draw(geo_coords, spei, overlay)            

    return Image.alpha_composite(target_image, overlay)
    