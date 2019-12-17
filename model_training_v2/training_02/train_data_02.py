import re

from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai
from model_training_v2.training_02.job_desc_02 import \
    _45f21e8cc59d13ba57e5ad2f0366fac7093672f223b8e7c119b45e16d4dc0f6c as D1
    # _e513f83c20942b5ecaa3a1247c154892802845c5eb3161201f4c0394d419a427 as D2, \
    # _c213b25d1182cce917971584991d1aef747d677967eb2dfc490ad45543554d1a as D3, \
    # _ae5f6f5c56847e54f10a1a6ba2fa3420744e630f7e6ce76c1f60bf3b4f128ce9 as D4, \
    # _9cb6da0cffb3173ef81c4fa03e3beda44459c5c0bf616acf3a043aaa9cba2329 as D5, \
    # _30ca4245355909d1dc9f89809c4d7158d6dce8c5f8ff36da555320db3aa80aff as D6, \
    # _516a36ab2091b8e70b7c6f638f1830cd0cf49a5e1d4ea93fc6c8b4840d678010 as D7, \
    # _1dd6b08b6221b5ebebcf086304b3f2c846eae4a71d833d26d53b250955de811a as D8, \
    # _ec4eec423b2b46859324e6f8df6bc44f635d51415a224fc13b36b9eacdf5c223 as D9, \
    # _ab44ba20db20d123646df89f89464e37995859d5cbf49b825b86ef32de354dc9 as D10

TRAIN_DATA = [
    (D1, {"entities": [(0, 18, ps), (71, 79, dv), (630, 638, dv), (1241, 1249, dv), (88, 103, ps), (129, 133, pd),
                       (188, 196, at), (197, 205, ql), (210, 216, ql), (958, 964, ql), (290, 301, pd), (277, 289, pd),
                       (348, 355, pd), (755, 762, pd),  (456, 472, pd), (696, 712, pd), (966, 974, ql), (616, 629, fw),
                       (991, 1004, fw), (1059, 1070, sf), (1042, 1049, pd), (1088, 1092, se), (1097, 1104, se),
                       (1250, 1257, se), (1155, 1165, ap), (1187, 1199, se), (1200, 1235, we), (1282, 1292, tm),
                       (1337, 1353, ge), (1318, 1331, ge), (1402, 1427, pd), (1499, 1503, at), (1504, 1508, dt),
                       (639, 642, pt), (1509, 1512, pt), (1559, 1563, pt), (1532, 1541, se), (1580, 1596, dv),
                       (1691, 1696, ap), (1727, 1748, ge), (1774, 1784, pl), (1804, 1811, fw), (1815, 1821, fw),
                       (1968, 1980, ge), (1982, 1996, sf), (2002, 2015, sf), (2070, 2094, ge), (2129, 2137, se),
                       (2152, 2162, tm), (2140, 2150, tm), (2279, 2295, of), (2327, 2344, of), (2453, 2469, tm),
                       (2479, 2497, of), (2532, 2547, of), (2569, 2575, of), (2788, 2794, pf), ]}),
    # (D2, {"entities": []}),
]

if __name__ == '__main__':
    word = "Github"

    from constants.constants import CONSTANTS_DICT

    start_index = [m.start() for m in re.finditer(word, D1)]
    full_index = [str(i) + ', ' + str(i + len(word)) for i in start_index]
    for index in full_index:
        _type = "None"
        for key, value in CONSTANTS_DICT.items():
            if word in value:
                _type = key
                break
        print('(' + index + ', ' + _type + ')', end=', ')

    # ent_dict = {}
    # for data in TRAIN_DATA:
    #     for entity in data[1]["entities"]:
    #         entity_type = entity[-1]
    #         entity_name = data[0][entity[0]: entity[1]]
    #         print(entity_name + ": " + entity_type)
    #         if entity_type not in ent_dict:
    #             ent_dict[entity_type] = [entity_name]
    #         else:
    #             ent_dict[entity_type].append(entity_name)
    # for k in ent_dict:
    #     print(k + ':', set(ent_dict[k]))
