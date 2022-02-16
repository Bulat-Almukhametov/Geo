from PIL import Image
from typing import Sequence

import myDraw.image
import myFiles.images
import myFiles.csv

csv_files = myFiles.csv.files()

template_image = myFiles.images.getMapTemplate()
images: Sequence[Image.Image] = []

for file_name in csv_files:
    points = myFiles.csv.read(file_name)

    target_image = myDraw.image.drawPointsLayer(template_image, points)

    myFiles.images.save(file_name, target_image)
    images.append(target_image)

myFiles.images.saveAnimation(images)