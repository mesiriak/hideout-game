

from base import BaseCreator
import json
import random
class PlayerCreator(BaseCreator):
    data = json.load(open("../card_data/players.json"))
    def creatCard(data):

        for i in range(3):
            dict_with_job = data[0]
            job = random.choice(list(dict_with_job.values()))
            dict_with_health = data[1]
            healthy = random.choice(list(dict_with_health.values()))
            dict_with_hobbi = data[2]
            hobbi = random.choice(list(dict_with_hobbi.values()))
            dict_with_fobia  = data[3]
            fobia = random.choice(list(dict_with_fobia.values()))
            dict_with_items = data[4]
            item = random.choice(list(dict_with_items.values()))
            dict_with_facts = data[5]
            fact = random.choice(list(dict_with_facts.values()))
            exp = random.randint(0,100)
            print(job)
            print(healthy)
            print(fobia)
            print(item)
            print(hobbi)
            print(fact)
            print("---next card---")

    creatCard(data)













