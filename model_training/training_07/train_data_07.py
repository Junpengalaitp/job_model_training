from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_07.job_desc_07 import *

TRAIN_DATA = [

     (D1, {'entities': [(2654, 2667, lf), (144, 148, pl), (1769, 1773, pl), (2725, 2729, pl), (4153, 4157, pl),
                        (4460, 4464, pl), (1967, 1972, ds), (4471, 4476, ds), (1977, 1985, ds), (4477, 4485, ds),
                        (2053, 2057, pf), (6333, 6337, pf), (2106, 2115, pt), (2194, 2198, pt), (4270, 4274, pt),
                        (3506, 3525, dv), (3527, 3542, dv), (4130, 4135, lf), (4465, 4470, lf), (6011, 6016, lf),
                        (4513, 4523, ap), (5994, 6003, lf), (6270, 6280, pl), (6300, 6305, lf), (6307, 6312, lf),
                        (6317, 6324, lf), (6329, 6332, lf), (6338, 6346, ap), (6347, 6353, pf), (6354, 6357, pl)]}),



]

if __name__ == '__main__':
    ent_dict = {}
    for data in TRAIN_DATA:
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            print(entity_name + ": " + entity_type)
            if entity_type not in ent_dict:
                ent_dict[entity_type] = [entity_name]
            else:
                ent_dict[entity_type].append(entity_name)
    for k in ent_dict:
        print(k, set(ent_dict[k]))