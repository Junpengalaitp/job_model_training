from model_training_algo.constants import pl, lf, cp, cs, pt, ds, dv, we, os_, ap, pf, ps, fd, ge, tl, at, ol
from model_training_v2.training_01.job_desc_01 import _5de37d02aa05ecc1e9502a54

TRAIN_DATA = [
    (_5de37d02aa05ecc1e9502a54, {
        "entities": [(17, 41, ps), (318, 328, pl), (346, 352, pl), (354, 360, pl), (390, 420, ds), (440, 443, pf),
                     (881, 884, pf), (365, 369, pl), (450, 458, pf), (476, 485, pf), (470, 474, ds), (487, 501, fd),
                     (552, 559, ap), (516, 540, ge), (561, 566, lf), (568, 571, tl), (573, 577, lf), (671, 678, ap),
                     (680, 685, ds), (707, 720, lf), (754, 766, at), (768, 775, ol), (873, 876, pf), (809, 836, fd),
                     (853, 867, ge), (968, 993, ap), (895, 901, pf), (906, 928, ap), (943, 952, ap), (954, 963, ap),
                     (1030, 1046, ps), (1156, 1163, dv), (1595, 1602, dv), (2433, 2440, dv),
                     (1206, 1234, ge), (1328, 1338, ap), (1239, 1246, ap), (1372, 1382, at), (1383, 1396, ap),
                     (1398, 1417, ap), (1422, 1435, ap), (1979, 1992, ap), (2292, 2308, dv), (1816, 1835, ge),
                     (1857, 1868, ge), (1994, 2004, ge), (2009, 2019, ge), (2055, 2075, ge), (2083, 2098, ge),
                     (2120, 2150, ge), (2163, 2185, ge), (2376, 2397, ge), (2417, 2428, ge), (2540, 2557, ge),
                     (2574, 2587, ge), ]}),
    # (D2, {"entities": []}),
    # (D3, {"entities": []}),
    # (D4, {"entities": []}),
    # (D5, {"entities": []}),
    # (D7, {"entities": []}),
    # (D8, {"entities": []}),
    # (D9, {"entities": []}),
    # (D10, {"entities": []})
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
