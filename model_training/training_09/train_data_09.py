from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_09.job_desc_09 import *

TRAIN_DATA = [

     (D1, {'entities': [(3670, 3673, os), (3675, 3682, os), (5980, 5987, ap), (6174, 6181, ap), (8520, 8527, ap),
                        (8034, 8040, ap), (8127, 8133, ap), (8205, 8211, ap), (8648, 8654, ap), (8661, 8667, ap),
                        (8674, 8680, ap), (1269, 1288, dv), (1600, 1619, dv), (2079, 2098, dv), (8871, 8890, dv),
                        (11345, 11364, dv), (12315, 12358, we), (12359, 12420, we), (12527, 12539, lf), (12521, 12526, lf),
                        (12540, 12547, lf), (12548, 12553, lf), (12554, 12558, lf), (12559, 12565, pl), (12566, 12569, pl),
                        (12153, 12166, lf), (10984, 10988, pf), (10804, 10809, pf), (10876, 10881, pf), (10934, 10939, pf),
                        (11709, 11727, dv)]}),
     (D2, {'entities': [(40, 57, dv), (1032, 1034, dv), (2806, 2808, dv), (6136, 6140, pl), (6142, 6145, pl), (6151, 6161, pl),
                        (6358, 6368, pl), (1328, 1335, lf), (6456, 6463, lf), (1340, 1347, pl), (6465, 6472, pl), (8790, 8797, pl),
                        (1321, 1326, lf), (6474, 6479, lf), (8779, 8784, lf), (6481, 6488, lf), (6494, 6499, lf), (8773, 8777, lf)]}),
     (D3, {'entities': [(476, 485, dv), (6810, 6812, dv), (6929, 6931, dv), (6984, 6989, dv), (7230, 7236, pl), (7237, 7244, ds),
                        (7273, 7286, lf), (7291, 7296, lf)]}),
     (D4, {'entities': []}),
     (D5, {'entities': []}),
     (D6, {'entities': []}),
     (D7, {'entities': []}),
     (D8, {'entities': []}),
     (D9, {'entities': []}),
     (D10, {'entities': []})



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