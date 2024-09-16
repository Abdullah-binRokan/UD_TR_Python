import os

def extract_place (filename):
    parts = filename.split('_')
    return parts[1]

def make_place_directories(places):
    for place in places:
        os.mkdir(place)

def orgnize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))

orgnize_photos("Photos")
