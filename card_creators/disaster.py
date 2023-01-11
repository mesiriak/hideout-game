import json,random
from base import BaseCreator


class DisasterCreator(BaseCreator):
    
    data = json.load(open("../card_data/disaster.json"))
    def disaster (data):

        disaster = random.choice(list(data.values()))
        print(disaster)
    disaster(data)
