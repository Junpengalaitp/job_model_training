from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_08.job_desc_08 import *

TRAIN_DATA = [

     (D1, {'entities': [(1071, 1106, we), (1112, 1122, pl), (2484, 2494, pl), (1142, 1149, lf), (2514, 2521, lf),
                        (1154, 1159, lf), (2526, 2531, lf), (1021, 1056, we), (1249, 1254, os), (1256, 1259, ap),
                        (1261, 1264, pf), (1472, 1496, dv), (1408, 1429, dv), (1656, 1664, ap), (1681, 1693, ap),
                        (2323, 2335, ap), (2636, 2648, ap), (4079, 4091, ap), (1382, 1394, ap), (2719, 2731, ap),
                        (2056, 2065, dv), (3843, 3852, dv), (1728, 1733, ap), (2443, 2478, we), (4190, 4238, we),
                        (4254, 4287, we), (1918, 1931, lf), (1911, 1915, pl), (2778, 2791, lf), (2792, 2802, dv),
                        (4353, 4363, dv), (2864, 2873, dv), (4425, 4434, dv), (2875, 2883, dv), (4436, 4444, dv),
                        (2750, 2762, pt), (2629, 2634, ap), (2337, 2359, ap), (2650, 2672, ap), (3723, 3745, ap),
                        (4093, 4115, ap), (2674, 2693, ap), (3747, 3766, ap), (2699, 2705, dv), (3768, 3774, dv)]}),



]

if __name__ == '__main__':
    ent_dict = {}
    for data in TRAIN_DATA:
        print(data[0])
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            print(entity_name + ": " + entity_type + ' ' + str(entity[0]) + ': ' + str(entity[1]))
            if entity_type not in ent_dict:
                ent_dict[entity_type] = [entity_name]
            else:
                ent_dict[entity_type].append(entity_name)
    for k in ent_dict:
        print(k, set(ent_dict[k]))