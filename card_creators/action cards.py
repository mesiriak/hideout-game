from base import BaseCreator
import json
import random, pprint


class PlayerCreator(BaseCreator):
    data = json.load(open("../card_data/action cards.json"))
    dict = data[0]
    action_cards = [[] for i in range(6)]
    for i in range(6):
        for q in range(2):

            action_cards[i].append(random.choice(list(dict.values())))
