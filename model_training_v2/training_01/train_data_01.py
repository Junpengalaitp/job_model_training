import re

from model_training_algo.constants import pl, lb, cs, pt, ds, dv, we, os_, ap, pf, ps, ge, tl, at, ol, sf, pd, fw, sv, \
    ql
from model_training_v2.training_01.job_desc_01 import _2923a7d6b1cf9df5993253768bb05ada370ce5e55d1772acf94bbcd41fac2e85 as D1, \
    _e513f83c20942b5ecaa3a1247c154892802845c5eb3161201f4c0394d419a427 as D2

TRAIN_DATA = [
    (D1, {
        "entities": [(17, 41, ps), (318, 328, pl), (346, 352, pl), (354, 360, pl), (405, 410, ds), (440, 443, pf),
                     (881, 884, pf), (365, 369, pl), (450, 458, pf), (476, 485, pf), (470, 474, ds), (487, 495, dv),
                     (552, 559, ap), (516, 540, ql), (561, 566, lb), (568, 571, tl), (573, 577, lb), (671, 678, ap),
                     (680, 685, ds), (707, 720, lb), (754, 766, at), (768, 775, ol), (873, 876, pf), (817, 825, dv),
                     (853, 867, pf), (983, 993, ap), (895, 901, pf), (906, 928, ap), (943, 952, ap), (954, 963, ap),
                     (1030, 1046, ps), (1156, 1163, dv), (1595, 1602, dv), (2433, 2440, dv), (1328, 1338, ap),
                     (1239, 1246, ap), (1372, 1382, at), (1383, 1396, at),
                     (1398, 1417, ap), (1422, 1435, ap), (1979, 1992, ap), (2292, 2308, ps), (1816, 1835, sf),
                     (1857, 1868, sf), (1994, 2004, sf), (2009, 2019, sf), (2055, 2075, sf), (2083, 2098, sf),
                     (2120, 2150, ge), (2163, 2185, ge), (2376, 2397, sf), (2417, 2428, sf), (2540, 2557, ql),
                     (2574, 2587, ge), ]}),
    (D2, {
        "entities": [(113, 124, ge), (126, 138, ge), (140, 150, ge), (1336, 1346, ge), (2394, 2404, ge), (233, 242, ge),
                     (257, 267, ge), (320, 336, ge), (748, 757, ge), (759, 770, ge), (776, 789, ge), (790, 819, dv),
                     (946, 950, pd), (4167, 4171, pd), (619, 626, pd), (998, 1003, ap), (1543, 1545, dv), (3619, 3622, dv),
                     (4741, 4743, dv), (2416, 2438, ap), (2446, 2448, dv), (2450, 2458, dv), (2460, 2484, ap), (3344, 3353, ap),
                     (2489, 2496, ap), (3015, 3026, ap), (3075, 3091, cs), (3113, 3163, we), (3181, 3196, pd), (3455, 3473, ql),
                     (3638, 3648, pl), (3515, 3519, pl), (4570, 4574, pl),
                     (3535, 3538, ds), (3574, 3579, os_), (3629, 3633, ol), (3634, 3637, ol), (3667, 3677, pl), (3712, 3722, pl),
                     (4759, 4769, pl), (3733, 3739, lb), (3757, 3780, pd), (3797, 3802, fw), (3807, 3814, fw), (3903, 3907, pt),
                     (3912, 3915, ol), (3948, 3951, tl), (3953, 3967, ap), (3969, 3977, tl), (3999, 4015, ap),
                     (3859, 3871, ap), (4347, 4359, ap), (4507, 4514, at), (4515, 4519, ds), (4520, 4523, pt), (4580, 4585, sv),
                     (4591, 4598, sv), (4603, 4615, cs), (4646, 4651, ds), (4658, 4665, lb), (4674, 4679, ds), (4684, 4691, ap),
                     (4719, 4735, ap), (4770, 4773, at), (4813, 4833, ap), (4843, 4862, ap), (5001, 5004, pf), (5025, 5031, pf),
                     (5042, 5048, tl), (5050, 5055, tl), (5057, 5061, fw), (5063, 5068, lb), (5070, 5076, tl), (5078, 5091, tl),
                     (5093, 5108, tl), (3412, 3425, ql), (3397, 3410, ql), ]}),
    # (D3, {"entities": []}),
    # (D4, {"entities": []}),
    # (D5, {"entities": []}),
    # (D7, {"entities": []}),
    # (D8, {"entities": []}),
    # (D9, {"entities": []}),
    # (D10, {"entities": []})
]

if __name__ == '__main__':
    word = "JAXB"

    from model_training_algo.constants import CONSTANTS_DICT
    start_index = [m.start() for m in re.finditer(word, D2)]
    full_index = [str(i) + ', ' + str(i + len(word)) for i in start_index]
    for index in full_index:
        _type = "None"
        for key, value in CONSTANTS_DICT.items():
            if word in value:
                _type = key
                break
        print('(' + index + ', ' + _type + ')', end=', ')

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
        print(k + ':', set(ent_dict[k]))
