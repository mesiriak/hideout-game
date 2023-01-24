import json, random
from base import BaseCreator


class DisasterCreator(BaseCreator):

    data = json.load(open("../card_data/disaster.json"))

    disaster = random.choice(list(data.values()))
    print(disaster)
