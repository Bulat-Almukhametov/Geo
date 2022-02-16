import csv
import os

import variables

def files():
    return [file[:-4] for file in os.listdir(variables.CSV_FOLDER) if file.endswith( '.csv')]

def read(file):
    points = []

    with open(f'{variables.CSV_FOLDER}/{file}.csv') as csvfile:
        csv_reader = csv.reader(csvfile)
        for index, row in enumerate(csv_reader):
            if index > 0:
                geo_coords = (float(row[3]), float(row[4]))
                spei = float(row[2])

                points.append((geo_coords, spei))

    return points