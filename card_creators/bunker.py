import random, json
from base import BaseCreator


class BunkerCreator(BaseCreator):
    square = random.randint(60, 480)
    rooms_in_bunker = 0
    size_of_bunker = ""
    if square <= 200:
        size_of_bunker = "small"
        rooms_in_bunker = 4
    if 200 < square <= 340:
        size_of_bunker = "medium"
        rooms_in_bunker = 6
    if square > 340:
        size_of_bunker = "big"
        rooms_in_bunker = 8
    data = json.load(open("../card_data/bunker.json"))
    name = data[0]

    size_of_bunker = name[size_of_bunker]
    print(size_of_bunker, square, rooms_in_bunker)
