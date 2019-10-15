from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_10.job_desc_10 import *

TRAIN_DATA = [

     (D1, {'entities': [(106, 118, dv), (1427, 1439, dv), (3161, 3164, ds), (2549, 2563, ds), (3270, 3284, ds), (3332, 3338, pl),
                        (3343, 3349, lf)]}),
     (D2, {'entities': [(2416, 2438, ap), (790, 819, dv), (2446, 2448, dv), (3667, 3677, pl), (3712, 3722, pl), (4759, 4769, pl),
                        (3515, 3519, pl), (3638, 3642, pl), (4570, 4574, pl), (3535, 3538, ds), (3733, 3739, lf), (4591, 4598, lf),
                        (3629, 3633, pl), (3634, 3637, pl), (3797, 3802, lf), (3807, 3814, lf), (4507, 4514, pt), (4515, 4519, ds),
                        (4520, 4523, pt), (4646, 4651, ds), (4658, 4665, lf), (4674, 4679, ds), (4580, 4585, lf), (4770, 4773, cp),
                        (1543, 1545, dv), (3619, 3621, dv), (4741, 4743, dv), (5001, 5004, pf), (5025, 5031, pf), (5033, 5040, lf),
                        (5042, 5048, lf), (5050, 5055, lf), (5057, 5061, lf), (5063, 5068, lf), (5070, 5076, pf), ]}),
     (D3, {'entities': [(105, 107, dv), (206, 208, dv), (110, 116, dv), (237, 243, dv), (1072, 1078, dv), (3803, 3809, dv),
                        (2734, 2741, pf), (4682, 4689, pf), (2743, 2749, pl), (2751, 2754, pl), (2756, 2766, pf), (2771, 2774, pf),
                        (4002, 4005, pf), (3035, 3047, dv), (3939, 3942, ap), (3944, 3947, ap), (3949, 3954, ap), (3956, 3959, ap),
                        (3964, 3968, ap), (4065, 4078, lf), (4021, 4024, pf), (4026, 4029, pf), (4031, 4033, pf), (4035, 4038, pf),
                        (4040, 4050, pf), (4110, 4115, os), (4209, 4214, ds), (4216, 4226, ds), (4571, 4587, lf), (514, 517, dv),
                        (2337, 2340, dv), (4975, 4978, dv), ]}),
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