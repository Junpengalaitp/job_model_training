from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_06.job_desc_06 import *

TRAIN_DATA = [

     (D1, {'entities': [(592, 604, lf), (749, 761, lf), (1342, 1354, lf), (6140, 6152, lf), (560, 565, lf),
                        (592, 597, lf), (1331, 1336, lf), (6026, 6031, lf), (6140, 6145, lf), (567, 577, pl), (729, 736, pf),
                        (579, 587, lf), (740, 748, lf), (1315, 1323, lf), (6153, 6161, lf), (631, 641, pl), (2652, 2654, dv),
                        (3353, 3355, dv), (10330, 10332, dv), (2655, 2665, ap), (1052, 1054, dv), (2676, 2678, dv),
                        (3429, 3431, dv), (10116, 10118, dv), (3562, 3564, ap), (4104, 4108, pl), (9946, 9950, pl),
                        (4109, 4113, lf), (6032, 6037, lf), (6038, 6042, lf), (6054, 6057, ap), (6416, 6419, ap),
                        (7328, 7331, ap), (9996, 9999, ap), (10679, 10682, ap), (6169, 6172, os), (6173, 6180, os),
                        (1219, 1226, lf), (1280, 1287, lf), (6181, 6188, lf), (6189, 6191, pl), (8514, 8517, dv),
                        (12909, 12912, dv), (7778, 7789, ap), (8018, 8029, ap), (11303, 11314, ap), (11365, 11376, ap),
                        (11556, 11567, ap), (11771, 11782, ap), (13326, 13337, ap)]}),
    (D2, {'entities': [(37, 47, dv), (1412, 1422, dv), (49, 55, pl), (1463, 1469, pl), (2107, 2113, pl), (2581, 2587, pl),
                       (1471, 1476, lf), (2333, 2338, lf), (1478, 1481, ds), (2221, 2224, ds), (2230, 2233, ds),
                       (1509, 1526, ap), (2159, 2165, lf), (2169, 2174, lf), (2214, 2224, ds), (2228, 2233, ds),
                       (2321, 2331, pl), (2340, 2344, pl), (2350, 2353, pl), (2354, 2358, lf), (6768, 6797, we)]}),
    (D3, {'entities': [(193, 198, os), (667, 672, os), (1735, 1740, os), (2204, 2209, os), (1854, 1859, pl),
                       (1875, 1878, os), (2214, 2217, os), (1723, 1762, we), (2014, 2017, cp), (2018, 2022, cp)]}),
    (D4, {'entities': [(164, 177, ap), (140, 147, dv), (148, 151, pt), (2689, 2698, pt), (2431, 2482, we),
                       (3096, 3100, os), (3101, 3107, os), (2614, 2617, pl), (2908, 2911, pl), (2625, 2631, pl),
                       (3134, 3137, pf), (2870, 2878, lf), (2945, 2948, ap), (3197, 3203, pf), (2983, 2986, lf),
                       (3228, 3232, pl), (3234, 3235, pl), (3236, 3239, pl), (3241, 3245, pl)]}),
    (D5, {'entities': [(149, 157, dv), (678, 686, dv), (1251, 1259, dv), (184, 200, dv), (204, 218, dv), (3232, 3246, dv),
                       (2081, 2095, ds), (2097, 2107, ds), (2159, 2162, pf), (2451, 2455, ds), (3412, 3416, ds),
                       (2457, 2462, ds), (3384, 3389, ds), (2464, 2468, ds), (3295, 3299, ds), (2528, 2531, ap),
                       (3930, 3933, ap), (893, 899, lf), (1345, 1351, lf), (1989, 1995, lf), (2590, 2596, lf),
                       (3265, 3271, lf), (3871, 3877, lf), (2613, 2618, lf), (2635, 2640, ds), (739, 744, lf),
                       (2654, 2659, lf), (2959, 2964, lf), (3391, 3396, lf), (2661, 2665, lf), (2966, 2970, lf),
                       (3301, 3305, lf), (3162, 3190, we), (3310, 3314, lf), (3406, 3410, pf), (2457, 2462, ds),
                       (3384, 3389, ds), (3455, 3459, pl), (780, 785, pl), (3461, 3466, pl), (3605, 3608, ds),
                       (3667, 3670, ds)]}),
    (D6, {'entities': [(170, 185, dv), (35, 37, dv), (209, 211, dv), (2593, 2595, dv), (2695, 2697, dv),
                       (1396, 1402, lf), (1404, 1414, lf), (1416, 1421, lf), (1423, 1428, lf), (1434, 1440, lf),
                       (1458, 1474, cs), (1499, 1514, cs), (1516, 1526, cs), (1528, 1541, cs), (1561, 1582, cs),
                       (1671, 1674, ds), (1693, 1704, cs), (1676, 1687, cs), (1718, 1725, lf), (1728, 1733, lf),
                       (1763, 1769, pf), (1774, 1780, pf), (2011, 2027, cs), (3681, 3684, dv), (3688, 3691, dv)]}),
    (D7, {'entities': [(346, 355, dv), (606, 612, lf), (779, 785, lf), (900, 906, lf), (1126, 1132, lf), (1566, 1572, lf),
                       (1594, 1600, lf), (581, 588, lf), (590, 595, lf), (597, 604, lf), (614, 621, ds), (1527, 1553, we),
                       (1652, 1659, ds), (623, 627, pf), (633, 638, ds), (1634, 1639, ds), (1554, 1583, we), (1641, 1646, ds),
                       (1684, 1693, dv), (1914, 1922, lf), (1819, 1822, ap), (1827, 1831, ap), (1727, 1732, pl),
                       (1734, 1738, pl), (1740, 1750, pl)]}),
    (D8, {'entities': [(442, 444, dv), (493, 505, lf), (524, 527, os), (1420, 1423, os), (1693, 1696, os), (532, 539, os),
                       (610, 617, os), (1408, 1415, os), (1701, 1708, os), (673, 679, pl), (709, 712, pf), (1850, 1855, ap)]}),
    (D9, {'entities': [(132, 139, lf), (974, 981, lf), (1342, 1349, lf), (969, 972, pl), (983, 993, pl), (995, 1000, pl),
                       (1002, 1006, pl)]}),
    (D10, {'entities': [(1647, 1653, os), (1719, 1725, pl), (1727, 1733, pl), (1745, 1749, pl), (1453, 1461, dv),
                        (1538, 1547, pf), (1707, 1717, pl)]})

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
    for k in ent_dict:
        print(k, set(ent_dict[k]))