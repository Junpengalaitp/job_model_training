from model_training_algo.constants import pl, lf, cs, pt, ds, dv, we, os_, ap, pf
from model_training.training_02.job_desc_02 import *

TRAIN_DATA = [
    (D1, {"entities": [(21, 26, lf), (280, 285, lf), (602, 614, lf), (786, 791, lf), (819, 831, lf), (1311, 1316, lf),
                       (1786, 1791, lf), (28, 33, lf), (286, 291, lf), (796, 801, lf), (1792, 1797, lf), (2298, 2303, lf),
                       (35, 42, lf), (44, 56, pt), (1928, 1940, pt), (58, 61, pl), (1900, 1903, pl), (94, 108, dv),
                       (495, 505, pl), (1205, 1224, dv), (1025, 1037, dv), (1892, 1895, pl), (1970, 1974, pt), (1717, 1750, we)]}),
    (D2, {'entities': [(429, 434, ap), (832, 837, ap), (995, 1005, pl), (1360, 1370, pl), (871, 889, dv), (891, 908, dv), (914, 931, dv),
                       (1007, 1016, lf), (1022, 1027, lf), (1458, 1463, lf), (1337, 1341, pl), (1343, 1346, pl), (1523, 1540, ap),
                       (1447, 1454, lf), (1566, 1571, lf), (1573, 1580, lf), (1585, 1595, lf)]}),
    (D3, {'entities': [(609, 616, os_), (929, 936, os_), (1098, 1105, os_), (1189, 1196, os_), (1354, 1361, os_), (1410, 1417, os_),
                       (1795, 1802, os_), (1889, 1896, os_), (1928, 1935, os_), (2153, 2160, os_), (2282, 2289, os_), (2520, 2527, os_),
                       (2693, 2700, os_), (2921, 2928, os_), (963, 979, dv), (1291, 1301, pt), (1280, 1286, pt), (2171, 2177, pl),
                       (3426, 3432, pl), (2182, 2186, pl), (3440, 3444, pl), (2496, 2515, we), (2611, 2621, cs), (2623, 2634, cs),
                       (3016, 3018, dv), (3455, 3458, ap)]}),
    (D4, {'entities': [(502, 518, dv), (523, 532, dv), (975, 988, lf), (2580, 2593, lf), (1000, 1008, ds), (1013, 1019, pf),
                       (2466, 2472, pf), (1600, 1603, dv), (2717, 2727, pl), (2729, 2734, pl), (2736, 2740, pl), (2746, 2758, pl),
                       (2385, 2390, ap), (2844, 2854, ds)]}),
    (D5, {'entities': [(1145, 1148, os_), (1152, 1159, os_), (1203, 1209, pt), (3180, 3186, pt), (1214, 1224, pt), (3188, 3198, pt),
                       (1307, 1316, dv), (1571, 1580, dv), (1671, 1680, dv), (1905, 1915, pl), (1917, 1920, pl),
                       (2527, 2530, pl), (1922, 1926, pl), (2533, 2537, pl), (2388, 2433, we), (2308, 2310, dv), (2482, 2484, dv),
                       (3111, 3116, ds), (3098, 3101, pf), (3118, 3128, ds), (3130, 3135, ds), (3155, 3158, pl), (3172, 3178, lf),
                       (3203, 3206, ap)]}),
    (D6, {'entities': [(452, 458, pl), (1565, 1571, pl), (463, 470, lf), (472, 480, lf), (1137, 1145, lf), (485, 496, lf),
                       (498, 505, ds), (507, 512, ds), (517, 522, ds), (549, 552, pf), (557, 567, pf), (710, 717, dv),
                       (722, 725, dv), (1177, 1187, pl), (1218, 1228, pl), (1442, 1447, pl), (1449, 1453, pl)]}),
    (D7, {'entities': [(52, 62, pf), (146, 156, pf), (485, 495, pf), (557, 567, pf), (788, 798, pf), (909, 919, pf),
                       (975, 985, pf), (1149, 1159, pf), (1263, 1273, pf), (1487, 1497, pf), (599, 604, pf), (606, 618, pf),
                       (620, 639, pf), (1197, 1202, ap), (1247, 1253, pl), (1374, 1380, pl), (1255, 1261, pf), (1298, 1304, pl),
                       (1390, 1394, pl)]}),
    (D8, {'entities': [(27, 39, lf), (121, 133, lf), (391, 403, lf), (772, 784, lf), (879, 891, lf), (1228, 1240, lf),
                       (1416, 1428, lf), (1442, 1454, lf), (143, 146, os_), (609, 612, os_), (151, 158, os_), (591, 598, os_),
                       (431, 441, dv), (458, 463, lf), (1313, 1318, lf), (467, 474, lf), (1322, 1329, lf), (486, 499, lf),
                       (1481, 1494, lf), (500, 507, pl), (1497, 1504, pl), (600, 604, pl), (1352, 1356, pl), (614, 625, pl),
                       (675, 680, lf), (762, 767, lf), (1343, 1348, pl)]}),
    (D9, {'entities': [(386, 395, lf), (1342, 1351, lf), (458, 468, pl), (488, 497, dv), (531, 534, ds), (911, 915, pl),
                       (918, 923, lf), (953, 958, lf)]}),
    (D10, {'entities': [(434, 453, we), (459, 472, lf), (472, 491, we), (499, 501, pl), (513, 516, lf)]})
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