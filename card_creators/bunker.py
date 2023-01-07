import random, json

from base import BaseCreator


class BunkerCreator(BaseCreator):
    
    data = json.load(open("../card_data/bunker.json"))

    bunker = random.choice(data)

    name = bunker["title"]
    

