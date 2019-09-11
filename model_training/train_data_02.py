from model_training.constants import pl, lf, cp, cs, pt, ds, dv, we, os, ap, pf
from model_training.job_desc_02 import *

TRAIN_DATA = [
    (D1, {"entities": [(21, 26, lf), (280, 285, lf), (602, 614, lf), (786, 791, lf), (819, 831, lf), (1311, 1316, lf),
                       (1786, 1791, lf), (28, 33, lf), (286, 291, lf), (796, 801, lf), (1792, 1797, lf), (2298, 2303, lf),
                       (35, 42, lf), (44, 56, pt), (1928, 1940, pt), (58, 61, pl), (1900, 1903, pl), (94, 108, dv),
                       (495, 505, pl), (1205, 1224, dv), (1025, 1037, dv), (1892, 1895, pl), (1970, 1974, pt), (1717, 1750, we)]}),
    (D2, {'entities': [(429, 434, ap), (832, 837, ap), (995, 1005, pl), (1360, 1370, pl), (871, 889, dv), (891, 908, dv), (914, 931, dv),
                       (1007, 1016, lf), (1022, 1027, lf), (1458, 1463, lf), (1337, 1341, pl), (1343, 1346, pl), (1523, 1540, ap),
                       (1447, 1454, lf), (1566, 1571, lf), (1573, 1580, lf), (1585, 1595, lf)]})
]

if __name__ == '__main__':
    ent_dict = {}
    for data in TRAIN_DATA:
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            print(entity_name + ": " + entity_type + data[0])
            if entity_type not in ent_dict:
                ent_dict[entity_type] = entity_name
            else:
                ent_dict[entity_type] += (', ' + entity_name)
    for k, v in ent_dict.items():
        print(k + ': ' + ent_dict[k])