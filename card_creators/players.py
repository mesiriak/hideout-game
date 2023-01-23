

from base import BaseCreator
import json
import random
class PlayerCreator(BaseCreator):
    data = json.load(open("../card_data/players.json"))
    mass_with_info = [[]for i in range(6)]
    index = 0


    for i in range(6):
        for k in range(6):
            dict_with_quality = data[k]
            quality = random.choice(list(dict_with_quality.values()))
            mass_with_info[index].append(quality)
        index += 1




















            # dict_with_job = data[0]
            # job = random.choice(list(dict_with_job.values()))
            # mass_with_info[index].append(job)
            # dict_with_health = data[1]
            # healthy = random.choice(list(dict_with_health.values()))
            # mass_with_info[index].append(healthy)
            # dict_with_hobbi = data[2]
            # hobbi = random.choice(list(dict_with_hobbi.values()))
            # mass_with_info[index].append(hobbi)
            # dict_with_fobia  = data[3]
            # fobia = random.choice(list(dict_with_fobia.values()))
            # mass_with_info[index].append(fobia)
            # dict_with_items = data[4]
            # item = random.choice(list(dict_with_items.values()))
            # mass_with_info[index].append(item)
            # dict_with_facts = data[5]
            # fact = random.choice(list(dict_with_facts.values()))
            # mass_with_info[index].append(fact)
            # if len(mass_with_info[index]) == 6 :
            #     index+=1
















