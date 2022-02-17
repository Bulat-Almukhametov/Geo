from PIL import Image
from typing import Sequence

import myDraw.image
import myDraw.title
import myDraw.palette
import myFiles.images
import myFiles.csv

csv_files = myFiles.csv.files()

template_image = myFiles.images.getMapTemplate()
images: Sequence[Image.Image] = []

for file_name in csv_files:
    points = myFiles.csv.read(file_name)

    target_image = myDraw.image.drawPointsLayer(template_image, points)
    target_image = myDraw.title.draw(file_name, target_image)
    target_image = myDraw.palette.draw(target_image)

    myFiles.images.save(file_name, target_image)
    images.append(target_image)

myFiles.images.saveAnimation(images)
