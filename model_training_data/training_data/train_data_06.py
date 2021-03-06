from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_data.training_text.job_desc_06 import \
    _e5940376daee8f1fb20214f55d73eab6614d1dc41b6b5e39f0510802281dca7c as D1, \
    _063e170581e747c183b3b59638892084aae5bb57b52ea00d18bf3e63987843d7 as D2, \
    _cbff4c37f44754e517f4206c7dc83d67ce672e9d19c4e3dbda59e548ba91f3d5 as D3, \
    _342049c6504576d0f397ff5a5227f10d8b041c3e49184eefbd9d642e5e16a07e as D4, \
    _42768d7b38b9a784a79f445a17a51957d3284fdaff307b9e75268c1b2776137d as D5, \
    _b6b0c1c0efdee8ce55c6d972713a08648eb23ed1e93df2295d4e0a364311754a as D6, \
    _e8e4ba8f369af5ff845013be42a637a74cc8b921e55d37823e94ef930cef5578 as D7, \
    _d54280607a1242c2cbe628ad5de99cbd4caebb4a626bb3ab2b6b381ff30f9da1 as D8, \
    _05d843a7745a3e837193f2e1b712551d60e45289aae6f7e1fabec68f223109f5 as D9, \
    _bda4774869819607aa33a891448c2ac94ca1db76360f6a957e4599ed4df795ad as D10

"""
    Entity order, separated by an empty line
    1. en_core_web_lg entities recognized but unrecognized by custom model
    2. correct entities recognized by custom model
    3. entities not recognized
    4. entities not recognized
"""

TRAIN_DATA = [
    (D1, {"entities": [
        (0, 7, 'ORG'),

        (33, 40, cp), (78, 101, ai),  (672, 674, 'GPE'), (681, 699, ps),
        (873, 883, pl), (913, 920, sv), (922, 925, pt), (939, 946, fw),
        (947, 952, fw), (1001, 1011, pf),
        (1366, 1369, pt), (1400, 1403, pt), (1404, 1416, se), (1450, 1455, lb),
        (1462, 1477, pd), (1631, 1634, pt), (1674, 1684, pl), (1779, 1784, lb),
        (1844, 1865, at), (1938, 1948, pf),
        (2018, 2025, cp), (2171, 2176, 'DATE'), (2191, 2207, ai),
        (2273, 2291, of), (2292, 2310, of), (2322, 2337, of),

        (803, 805, ai), (786, 789, pd), (954, 977, ap), (979, 984, ds), (791, 797, pd), (385, 411, ai),
        (985, 990, lb), (991, 997, pf), (1196, 1203, cp), (1284, 1307, tm), (1489, 1518, ql),
        (1620, 1624, sv), (1646, 1670, ql), (1685, 1695, sf), (1608, 1619, se), (1719, 1730, se),
        (1767, 1778, se), (1337, 1347, se), (1372, 1382, se), (1593, 1603, se), (1731, 1752, ap),
        (1813, 1826, ql), (1904, 1911, sv), (1960, 1969, pf), (2081, 2097, tm), (2209, 2224, ai),
        (2250, 2272, of), (1535, 1545, ps),
        ]}),
    (D2, {"entities": [
        (819, 836, 'GPE'), (2591, 2595, 'CARDINAL'), (2696, 2716, 'TIME'), (2762, 2768, 'TIME'),
        (2804, 2816, 'MONEY'), (2852, 2869, 'GPE'), (3180, 3193, 'TIME'),

        (148, 152, 'DATE'), (841, 847, 'GPE'), (1503, 1509, fw),
        (1733, 1740, pl), (1784, 1792, at), (1794, 1800, pl), (1834, 1861, pd),
        (1875, 1885, tl), (1996, 2002, pl), (2003, 2009, fw), (2119, 2125, pl), (2140, 2146, fw),
        (2152, 2162, pl), (2874, 2880, 'GPE'),

        (1703, 1717, ql), (1801, 1808, fw), (1961, 1967, pt), (2010, 2013, fw), (2014, 2020, pd),
        (1568, 1578, lb),

        (41, 66, ps), (1593, 1613, se),  (1626, 1645, ds), (1545, 1555, se), (1756, 1766, se), (2443, 2453, ps),
        (1905, 1912, os_), (2282, 2304, of), (2504, 2517, sf), (2578, 2589, of), (194, 204, ps), (3143, 3153, ps),
        (3252, 3262, ps),
    ]}),
    (D3, {"entities": [
        (524, 547, 'PRODUCT'), (993, 999, 'ORG'), (1771, 1772, 'CARDINAL'), (1934, 1935, 'CARDINAL'),
        (2008, 2014, 'PERSON'), (2083, 2084, 'CARDINAL'),

        (94, 99, 'CARDINAL'), (153, 155, 'NORP'), (279, 282, 'NORP'), (304, 306, 'GPE'),
        (468, 472, pt), (494, 508, pd), (635, 645, 'DATE'), (744, 757, lb), (759, 764, ds), (766, 775, at),
        (777, 795, pf), (797, 806, pd), (883, 905, ap), (1349, 1361, ap), (1363, 1375, ap), (1451, 1462, pd),
        (1511, 1533, ge), (1572, 1579, cp), (1634, 1635, 'CARDINAL'), (1652, 1656, pt),
        (1680, 1694, pd), (1766, 1769, pt), (1990, 1995, tl),
        (2097, 2103, pf), (2138, 2141, pl), (2148, 2149, 'CARDINAL'),

        (0, 9, 'ORG'),  (160, 168, 'ORG'), (598, 610, dv), (720, 724, pl), (726, 737, fw), (739, 742, se),  (875, 878, ap),
        (1315, 1327, ql), (1377, 1390, ql), (1592, 1608, tm), (1866, 1874, ql),

        (21, 46, tm), (577, 593, dv), (649, 670, we), (836, 859, 'PRODUCT'), (1017, 1045, tm), (1417, 1434, sf),
        (1793, 1807, lb), (1876, 1883, ql), (1885, 1897, ql),

    ]}),
    (D4, {"entities": [
        (1949, 1950, 'CARDINAL'), (2013, 2033, 'TIME'),  (2142, 2163, 'TIME'),

        (403, 412, ps), (862, 865, pt), (901, 913, se), (923, 928, tl),
        (1018, 1020, 'GPE'), (1089, 1104, ps), (1468, 1484, ps), (1979, 1996, of), (2501, 2505, pl),
        (2530, 2533, ol), (2534, 2538, ol), (2571, 2580, lb),
        (2628, 2638, pl), (2643, 2653, pl), (2673, 2678, lb), (2680, 2686, lb), (2688, 2700, pl),
        (2728, 2732, os_), (2733, 2738, os_), (2739, 2743, ol), (2748, 2753, ds),
        (2769, 2774, ds), (2790, 2803, lb), (2996, 3004, at),

        (854, 857, pd), (930, 940, pf), (2487, 2500, fw), (2507, 2513, pl), (2523, 2528, pl), (2557, 2569, fw),
        (2596, 2608, fw), (2705, 2708, pl), (2744, 2747, pt), (2962, 2965, pt), (2967, 2972, sv), (3210, 3215, lb),
        (3216, 3221, pl), (3222, 3227, fw), (3228, 3234, lb), (3235, 3241, pl), (3175, 3185, pf),

        (537, 543, dv), (884, 900, pd), (942, 946, tl), (1495, 1515, sf), (1911, 1922, of), (1893, 1907, sf),
        (2939, 2946, sv), (3043, 3058, ge), (3063, 3081, sf), (417, 426, ps),  (1783, 1791, ps), (3186, 3195, ps),
    ]}),
    (D5, {"entities": [
        (895, 899, 'PERCENT'), (1116, 1127, 'ORG'), (1894, 1905, 'ORG'), (197, 203, 'GPE'),

        (25, 40, pd), (84, 86, 'GPE'), (187, 193, 'GPE'), (346, 351, 'DATE'),
        (429, 437, 'ORG'), (451, 456, 'ORG'), (489, 500, 'ORG'), (545, 562, 'ORG'), (1011, 1026, pd),
        (1052, 1059, os_), (1212, 1219, os_), (1229, 1238, 'CARDINAL'),
        (1335, 1342, os_), (1545, 1553, 'DATE'), (1617, 1621, pl),
        (1665, 1672, os_),

        (172, 185, 'GPE'), (415, 421, 'ORG'), (423, 427, 'ORG'), (439, 445, 'ORG'), (502, 528, 'ORG'), (530, 535, 'ORG'),
        (537, 543, 'ORG'), (568, 578, 'PERSON'), (594, 605, tm), (1130, 1141, tm), (1315, 1327, at), (1557, 1601, we),
        (1626, 1632, pl),

        (837, 853, tm),  (65, 69, 'MONEY'), (1112, 1114, dv), (1715, 1724, at), (1742, 1751, lb), (1759, 1770, sf),
        (1776, 1806, sf), (769, 777, ps), ]}),
    (D6, {"entities": [
        (280, 286, 'GPE'), (425, 431, 'GPE'),

        (63, 84, ps), (105, 111, 'ORG'), (116, 131, 'ORG'), (133, 140, 'GPE'), (148, 167, pf),
        (168, 180, dv), (181, 197, ai), (205, 211, pl), (269, 275, 'ORG'), (315, 318, os_),
        (414, 420, 'ORG'), (460, 467, os_), (475, 479, pl), (526, 532, 'ORG'),

        (468, 474, pd),

        (198, 204, pl), (255, 258, os_), (480, 486, pl), (319, 330, pl), (331, 336, pl), (337, 345, os_),
        (95, 104, ps), (259, 268, ps), (404, 413, ps), (396, 403, os_), ]}),
    (D7, {"entities": [
        (492, 499, 'TIME'),

        (128, 143, pd), (187, 193, 'PERSON'),
        (378, 394, 'MONEY'), (427, 434, os_), (468, 479, se),
        (566, 577, se), (589, 593, pl), (602, 612, pl), (617, 620, pl),
        (1126, 1134, 'DATE'), (1224, 1228, pl),
        (1230, 1233, pl), (1235, 1245, pl), (1250, 1256, pl), (1335, 1342, os_),
        (1464, 1467, pl), (1472, 1476, pl),
        (1534, 1540, tl), (1591, 1598, os_), (1600, 1603, os_), (1605, 1610, os_), (1626, 1628, dv),
        (1633, 1645, ap), (1650, 1657, os_), (1696, 1699, tl), (1753, 1767, ge), (1852, 1856, pl),


        (153, 165, tl), (167, 182, tl), (337, 349, tl), (541, 553, tl), (351, 354, tl), (435, 438, tl),
        (554, 557, tl), (1343, 1346, tl), (440, 454, lb), (594, 600, pl), (1138, 1169, we), (1420, 1431, cs),
        (1216, 1222, pl), (1477, 1483, pl), (699, 705, pd), (797, 801, tl), (2464, 2468, tl), (1501, 1517, tl),
        (1735, 1742, 'LANGUAGE'), (1991, 1999, 'LANGUAGE'), (459, 467, tl), (959, 967, tl), (1524, 1527, os_),
        (1432, 1445, cs),


        (25, 45, pd), (230, 233, pd), (1282, 1285, pd), (1671, 1686, se), (780, 789, ql), (1107, 1109, dv),
        (1775, 1788, ge),
    ]}),
    (D8, {"entities": [
        (3, 9, 'GPE'), (187, 193, 'GPE'), (1551, 1563, 'CARDINAL'),

        (294, 311, pd), (555, 577, at), (592, 608, ai), (853, 860, os_), (1080, 1099, tm),
        (1155, 1163, 'WORK_OF_ART'), (1250, 1254, pl), (1263, 1270, os_),
        (1564, 1571, dv), (1600, 1604, pl),

        (517, 533, ql), (543, 554, ql), (628, 642, cp), (1271, 1274, tl), (1340, 1380, sf), (1314, 1339, ge),
        (1473, 1485, cs), (1528, 1534, pl), (1593, 1594, pl), (1609, 1614, pl), (1457, 1463, lb),

        (15, 24, ps), (194, 203, ps), (368, 377, ps), (220, 235, ge), (792, 802, se), (930, 940, se), (815, 825, se),
        (830, 845, se), (1285, 1300, se), (955, 966, se), (982, 993, se), (241, 253, ge), (682, 709, cp),
        (1023, 1036, at), (1225, 1244, we), (1385, 1405, sf), (1589, 1591, pl), ]}),
    (D9, {"entities": [
        (327, 338, 'CARDINAL'), (1423, 1429, 'PRODUCT'),

        (430, 453, at),
        (701, 706, ds), (707, 713, pl),
        (715, 720, lb), (722, 725, pl), (726, 729, pf), (866, 878, ge),
        (959, 963, 'DATE'), (1088, 1106, 'DATE'), (1171, 1212, pd), (1213, 1229, 'DATE'),
        (1257, 1263, pf), (1264, 1270, pf), (1272, 1274, ap), (1292, 1300, pf), (1500, 1503, pf),
        (1548, 1551, pf), (1556, 1562, pf),

        (668, 672, dt), (674, 678, dt), (692, 696, ds), (883, 901, ge), (1275, 1277, ap), (1515, 1517, fw),
        (1318, 1329, pd), (1460, 1472, cs), (646, 656, tl), (634, 644, tl), (658, 667, pf), (1505, 1508, cs),

        (189, 195, dv), (486, 492, dv), (1522, 1528, dv), (377, 381, pl), (607, 611, pl), (954, 958, pl), (419, 425, dv),
        (497, 511, se), (1533, 1547, se), (200, 211, se), (1146, 1157, se), (1411, 1422, se), (613, 617, ol),
        (618, 627, fw),  (687, 691, ol),  (745, 752, pf), (466, 476, cp), (1406, 1410, pf),
        (976, 980, ol), (981, 990, ps), (998, 1013, cs), (1050, 1059, cs), (1064, 1076, cs), (1077, 1087, cs),
        (1230, 1238, pf), (273, 281, pf), (454, 460, cp),

    ]}),
    (D10, {"entities": [
        (16, 23, 'ORG'), (147, 165, pd), (368, 388, dv),
        (442, 444, dv), (493, 505, lb), (524, 527, os_), (532, 539, os_), (610, 617, os_),
        (673, 679, pl), (709, 712, pf), (722, 732, dv), (836, 846, 'GPE'), (876, 882, 'GPE'), (884, 890, 'GPE'),
        (1067, 1075, 'GPE'), (1113, 1115, 'GPE'), (1157, 1159, 'GPE'), (1213, 1217, 'NORP'),
        (1257, 1275, pd), (1313, 1324, pd), (1408, 1415, os_), (1420, 1423, os_), (1693, 1696, os_), (1701, 1708, os_),

        (56, 75, cp), (166, 175, ps), (1276, 1285, ps), (1377, 1387, ps), (190, 207, cp), (220, 227, 'ORG'),
        (390, 410, se), (510, 514, pl), (568, 572, pl), (590, 597, os_), (750, 772, se), (1088, 1095, 'GPE'),
        (1495, 1513, ge), (475, 481, pd), (1763, 1769, pd), (1770, 1785, se), (1850, 1852, ap), (1853, 1855, ap),
    ]})
]

if __name__ == '__main__':
    word = "OOP"

    print_entities(TRAIN_DATA)

    entity_finder(word, D3)
