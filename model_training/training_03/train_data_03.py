from constants.category import pl, lb, cs, pt, ds, dv, we, os_, ap, pf
from model_training.training_03.job_desc_03 import *

TRAIN_DATA = [
    (D1, {'entities': [(657, 660, os_), (1412, 1415, os_), (1493, 1496, os_), (1891, 1894, os_), (665, 672, os_), (1420, 1427, os_),
                       (1501, 1508, os_), (1918, 1925, os_), (705, 715, ap), (1040, 1050, ap), (1232, 1242, ap), (1740, 1774, we),
                       (1816, 1859, we), (1896, 1901, pl), (1903, 1914, pl), (1927, 1931, pl), (1933, 1939, pl), (1606, 1612, pl),
                       (1976, 1982, pl), (1623, 1625, pl), (1984, 1986, pl), (1614, 1618, pl), (1988, 1992, pl)]}),
    (D2, {'entities': [(23, 33, dv), (34, 47, dv), (183, 189, pl), (476, 482, pl), (1038, 1044, pl), (191, 201, pl), (270, 280, pl),
                       (492, 502, pl), (206, 209, pl), (265, 268, pl), (484, 487, pl), (1034, 1037, pl), (285, 290, ds), (1088, 1091, ap),
                       (1141, 1163, ap), (1049, 1052, pt), (1108, 1113, ap), (1116, 1121, ap), (1198, 1213, cs)]}),
    (D3, {'entities': [(179, 181, pl), (306, 308, pl), (183, 187, lb), (313, 317, lb), (191, 194, pl), (337, 350, ap)]}),
    (D4, {'entities': [(25, 44, dv), (525, 544, dv), (870, 873, pf), (1459, 1462, pf), (2246, 2249, pf), (887, 893, pf),
                       (895, 903, ds), (905, 911, pl), (1001, 1007, pl), (1529, 1535, pl), (2580, 2586, pl),
                       (1060, 1064, pl), (2002, 2006, pl), (919, 932, lb), (1066, 1074, lb), (1119, 1130, dv), (1174, 1183, dv),
                       (1537, 1540, ds), (2606, 2609, ds), (913, 917, pl)]}),
    (D5, {'entities': [(136, 145, lb), (445, 454, lb), (1252, 1261, lb), (1876, 1885, lb), (5685, 5694, lb),
                       (5800, 5809, lb), (1793, 1796, dv), (2860, 2863, pl), (2889, 2894, ap), (3023, 3032, ap), (3034, 3039, ap),
                       (3041, 3046, ap), (2400, 2444, we)]}),
    (D6, {'entities': [(33, 36, pl), (771, 774, pl), (1538, 1541, pl), (1536, 1537, pl), (1588, 1595, os_)]}),
    (D7, {'entities': [(25, 41, lb), (79, 95, lb), (210, 226, lb), (589, 605, lb), (659, 675, lb), (843, 849, dv),
                       (864, 870, pf), (875, 885, pf), (907, 910, pf), (913, 916, pf)]}),
    (D8, {'entities': [(1070, 1126, we), (253, 256, pf), (1218, 1223, pl), (1228, 1232, pl)]}),
    (D9, {'entities': [(489, 494, ds),  (1490, 1495, ds),  (1818, 1823, ds), (195, 202, ds),  (1479, 1486, ds), (1781, 1788, ds),
                       (946, 952, ds),  (966, 972, ds),  (1007, 1013, ds), (1349, 1355, ds), (1036, 1037, pl), (1042, 1045, pl),
                       (1471, 1474, ds)]}),
    (D10, {'entities': [(1011, 1015, lb), (2233, 2237, lb), (2659, 2666, lb), (2701, 2708, lb), (2244, 2249, ds), (2873, 2878, ds),
                        (2252, 2262, pf), (2656, 2658, pl), (2754, 2762, pt), (2763, 2767, ds)]})
]

if __name__ == '__main__':
    ent_dict = {}
    for data in TRAIN_DATA:
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            print(entity_name + ": " + entity_type + ' ' + str(entity[0]) + ': ' + str(entity[1]))
            if entity_type not in ent_dict:
                ent_dict[entity_type] = [entity_name]
            else:
                ent_dict[entity_type].append(entity_name)