from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_data.training_text.job_desc_08 import\
    D1_00681308cba170c3ce8c5b21519bff1606d8051f1bfbad333507d5908f7dcc03 as D1, \
    D2_00a65f8b1c231209dc87a36ebb4368633f9efb4b066f63fbacd887206da380ce as D2, \
    D3_bb4ce9a8e7a058a95a71fc4fb7eb19fc88682a30ebdbcb82c6d2a1bbfc2aadcc as D3, \
    D4_02c1fd622a616e2fd1342b5f36ee629892b4d35f44b02b0623055e1c33da55f3 as D4, \
    D5_9fff53da4939873b545574ffcd62419d6133d44abce0a7b66f2cf4df127a1335 as D5, \
    D6_d26db8a297034571b0c6bba43468e5bbbe249bdaf2fc5fecf6b023dedbb5b3a0 as D6, \
    D7_05cc01c480e91e1cff581094b0cb8733aa87fcbe5bb05d83f348b9d7f7824480 as D7, \
    D8_8ff8d158757cc9b7c53109e58f5be52820be50ccdc86dac04b7933b5c6731f20 as D8, \
    D9_07b408643d9907a732026749b0557019bb1ab83428d9b1e4fd609f998202f193 as D9, \
    D10_23635e94f534e182a8dd82030c06c9b5c56280a1829b72cc79c5d176a103cec0 as D10

"""
    Entity order, separated by an empty line
    1. en_core_web_lg entities recognized but unrecognized by custom model
    2. correct entities recognized by custom model
    3. entities not recognized
"""

TRAIN_DATA = [
    (D1, {"entities": [
        (9, 12, 'ORG'), (47, 58, 'PRODUCT'), (89, 92, 'ORG'), (193, 215, 'ORG'), (332, 335, 'ORG'), (426, 429, 'ORG'),
        (622, 635, 'CARDINAL'), (792, 795, 'ORG'), (1236, 1241, 'ORDINAL'), (1317, 1321, 'DATE'), (1323, 1347, 'ORG'),
        (1434, 1437, 'ORG'),  (1946, 1952, 'LOC'), (1957, 1962, 'GPE'), (1744, 1757, 'ORG'), (1729, 1737, 'ORG'),
        (1759, 1772, 'ORG'),

        (0, 3, 'ORG'), (24, 25, 'CARDINAL'), (119, 137, ps), (168, 176, 'GPE'), (178, 180, 'GPE'),
        (552, 561, 'DATE'), (563, 573, we), (586, 589, ol), (591, 597, ds), (606, 616, we), (650, 659, 'DATE'),
        (661, 671, we), (689, 695, fw), (730, 734, ds), (751, 761, we),
        (806, 812, fw), (838, 868, sf), (876, 887, sf), (926, 931, ap),
        (1349, 1352, 'ORG'), (1398, 1409, se), (1425, 1428, 'ORG'),
        (1449, 1450, 'CARDINAL'), (1477, 1500, se), (1502, 1524, se),
        (1562, 1595, 'ORG'), (1639, 1657, dv), (1690, 1708, 'ORG'), (1710, 1727, 'ORG'),
        (1739, 1742, 'ORG'), (1774, 1788, 'ORG'), (1799, 1804, 'GPE'),
        (1815, 1823, 'GPE'), (1834, 1843, 'GPE'), (1854, 1861, 'GPE'), (1907, 1910, 'ORG'), (1931, 1944, 'GPE'),

        (601, 604, ds), (723, 728, dt), (740, 745, ds), (819, 824, dt), (893, 903, we), (949, 961, ge), (1256, 1274, ps),
        (1526, 1538, pd), (1546, 1560, ds),
        ]}),
    (D2, {"entities": [
        (16, 23, 'ORG'), (917, 920, 'ORG'), (1050, 1070, 'PRODUCT'), (1471, 1474, 'ORG'), (2919, 2931, 'CARDINAL'),
        (6946, 6949, 'ORG'), (7209, 7212, 'ORG'),

        (558, 564, dv), (669, 680, se), (1385, 1400, ge), (2561, 2571, we),
        (2574, 2575, 'CARDINAL'), (2740, 2751, se), (2789, 2796, se), (2798, 2800, dv),
        (2842, 2850, 'DATE'), (2851, 2861, we), (2987, 2997, we), (3011, 3015, pt), (3042, 3045, pt), (3046, 3052, dv),
        (3109, 3117, ps), (3129, 3132, pt), (3377, 3387, we), (3391, 3396, tl), (3403, 3422, se),
        (3427, 3434, se), (3703, 3710, se),
        (3751, 3763, pd), (3766, 3770, at), (3785, 3789, dt), (3878, 3888, we),
        (3924, 3928, at), (3929, 3932, pt), (3937, 3941, pt), (3978, 3981, pd),
        (3990, 3996, dv), (4039, 4049, we), (4103, 4106, pt),
        (4246, 4250, pt), (4273, 4283, we), (4327, 4334, 'DATE'), (4365, 4375, we), (4413, 4420, ds),
        (4421, 4426, ds), (4428, 4434, fw), (4498, 4500, ap), (4501, 4503, ap), (4515, 4519, os_), (4562, 4567, ap),
        (4760, 4779, ap), (4987, 5002, ap), (5012, 5031, ap), (5175, 5181, dv), (5186, 5200, se), (5503, 5509, dv),
        (5638, 5648, se), (5956, 5958, dv), (6290, 6308, dv), (6310, 6313, 'ORG'),
        (7254, 7271, of),
        (7305, 7318, 'GPE'), (7429, 7446, 'GPE'),

        (2601, 2620, cp), (2621, 2631, we), (2766, 2784, dv), (2867, 2875, pf), (2877, 2883, tl), (3081, 3089, pf),
        (3435, 3445, dv), (3501, 3511, we), (3540, 3543, dt), (4237, 4240, dt), (3579, 3582, ol),
        (3790, 3793, ol), (3594, 3598, ol), (3610, 3621, se), (3637, 3647, we), (3777, 3781, ol), (3900, 3904, ol),
        (4003, 4007, ol), (4009, 4014, ol), (4016, 4023, fw), (4231, 4235, pt), (4296, 4300, pd), (4315, 4325, pf),
        (4956, 4975, ap), (5039, 5062, ap), (5064, 5067, ap), (5073, 5102, ap), (5104, 5107, ap), (5246, 5265, ap),
        (5553, 5565, at), (5891, 5901, ps), (5845, 5853, ps), (5863, 5872, ps), (6246, 6250, se), (6386, 6397, se),
        (6482, 6489, se), (6461, 6468, se), (3301, 3310, ol), (3515, 3538, dt), (3861, 3867, tl),
    ]}),
    (D3, {"entities": [
        (52, 59, 'GPE'), (61, 63, 'GPE'),

        (0, 10, 'ORG'), (81, 105, ps), (227, 237, se), (246, 261, pd), (302, 321, pd), (704, 715, se),
        (732, 743, pd), (847, 864, ps), (993, 1007, ap), (1071, 1080, 'DATE'), (1084, 1094, we),
        (1138, 1142, pl), (1150, 1156, pl), (1158, 1163, pl), (1213, 1215, ap), (1216, 1218, ap), (1257, 1264, tl),
        (1477, 1484, os_), (1489, 1492, os_), (1695, 1701, dv), (1783, 1791, ds),
        (1971, 1982, pf), (2167, 2179, at), (2206, 2211, ds), (2253, 2258, ds), (2260, 2273, lb), (2279, 2299, ds),

        (270, 277, fw), (323, 334, se), (1624, 1635, se), (335, 350, ql), (354, 369, ql), (371, 386, ql), (415, 438, ql),
        (835, 841, sf), (865, 876, ap), (916, 928, ql), (1144, 1148, pl), (1247, 1255, tl), (1295, 1311, ap), (1371, 1393, ge),
        (1451, 1457, pd), (1506, 1516, we), (1595, 1612, ps), (1740, 1766, ap), (1803, 1821, pf), (1903, 1910, lb),
        (1915, 1921, lb), (1948, 1960, se), (1995, 2001, pf), (2123, 2126, pd), (2127, 2130, pt), (2152, 2157, pt),
        (2159, 2162, at),
    ]}),
    (D4, {"entities": [
        (17, 30, ps), (41, 47, 'GPE'), (49, 51, 'GPE'), (56, 65, 'GPE'), (67, 69, 'GPE'), (132, 148, cs), (166, 181, 'DATE'),
        (185, 195, we), (208, 228, se), (229, 244, 'DATE'), (248, 258, we), (278, 288, pf), (290, 296, pf),
        (355, 360, ap), (421, 425, pl), (427, 437, pl), (439, 445, pl), (447, 452, pl), (486, 505, ds),
        (533, 550, ap), (588, 591, tl), (593, 597, tl), (644, 654, cs), (714, 719, os_), (761, 776, se),
        (1222, 1250, tm), (1285, 1305, ds), (1310, 1313, ol), (1391, 1397, fw),
        (1417, 1422, fw),

        (10, 16, dv), (262, 267, pf), (468, 474, dv), (518, 521, ds), (627, 642, cs), (721, 725, os_), (810, 830, sf),
        (1399, 1404, ds), (1406, 1415, ds), (1427, 1432, dt), (951, 970, cp), (454, 460, sv), (1354, 1374, at)
    ]}),
    (D5, {"entities": [
        (61, 68, 'GPE'), (70, 72, 'ORG'), (102, 109, 'GPE'), (111, 113, 'ORG'),

        (37, 41, fw), (81, 85, fw), (199, 211, ds), (329, 339, se), (366, 376, se),
        (698, 708, se), (1214, 1229, se), (1316, 1331, se), (1502, 1517, se),
        (1574, 1582, 'WORK_OF_ART'), (1599, 1615, cs), (1732, 1739, 'GPE'),
        (1758, 1766, 'ORG'),

        (173, 179, pl), (181, 183, pl), (185, 192, fw), (223, 227, os_), (278, 288, at), (388, 394, tl),
        (1464, 1466, cp), (1595, 1597, cp),
        ]}),
    (D6, {"entities": [

        (0, 22, ps), (27, 49, ps), (90, 99, se), (101, 111, se), (387, 394, se),
        (417, 434, ap), (639, 661, ps), (1013, 1015, dv), (1047, 1056, ql),
        (1099, 1109, we), (1278, 1288, pl), (1307, 1315, fw), (1346, 1357, se), (1431, 1434, pd),
        (1439, 1458, pd), (1944, 1956, at), (1982, 1985, pd), (2005, 2010, lb),
        (2012, 2019, sv), (2021, 2028, fw), (2030, 2038, fw), (2088, 2094, pf), (2185, 2196, sf),
        (2229, 2251, ge), (2794, 2805, se), (2851, 2855, pt), (2894, 2895, 'CARDINAL'),
        (2899, 2909, 'DATE'), (2938, 2948, we), (2963, 2966, pd), (2971, 2990, pd), (3017, 3022, ap),

        (332, 354, ps), (451, 473, ps), (499, 521, sf), (527, 546, sf), (153, 168, ap), (608, 623, ap), (1248, 1263, ap),
        (2922, 2937, ap), (675, 691, tm), (1073, 1097, ql), (1670, 1684, ps), (1688, 1701, se), (78, 87, se), (739, 748, se),
        (1598, 1607, se), (1970, 1981, pd), (2040, 2046, tl), (2051, 2066, pf), (2096, 2109, pf), (2111, 2126, pf),
        (2144, 2154, pf), (2128, 2138, pf), (2263, 2285, ge), (2733, 2737, pd), (2722, 2727, pf), (2823, 2842, pd),
        (3066, 3085, ql),
    ]}),
    (D7, {"entities": [
        (59, 66, 'GPE'), (109, 124, 'WORK_OF_ART'), (360, 372, 'CARDINAL'), (531, 543, 'CARDINAL'),

        (0, 17, ps), (95, 103, 'WORK_OF_ART'), (128, 144, cs), (169, 182, 'DATE'), (195, 205, we),
        (217, 219, dv), (265, 270, lb), (273, 282, fw), (376, 379, ol),
        (395, 399, ol), (401, 405, ol), (414, 424, we), (441, 444, pl), (446, 456, pl), (470, 473, ol), (544, 546, dv),
        (558, 567, lb), (587, 594, fw), (630, 639, ps), (662, 667, tl),
        (669, 673, tl), (675, 682, tl), (717, 727, se), (755, 765, we), (828, 838, we),
        (852, 856, pt), (925, 935, pl), (991, 997, dv), (999, 1009, we), (1024, 1036, ap), (1050, 1060, se),
        (1068, 1087, pd), (1167, 1174, tl),
        (1264, 1282, sf), (1284, 1297, sf), (1302, 1321, sf), (1453, 1471, se), (1704, 1713, dv), (1720, 1728, dv),
        (1735, 1744, ps), (1770, 1780, we), (1850, 1860, we), (1905, 1915, ps), (2009, 2025, cs),
        (2148, 2176, of), (2202, 2232, of), (2465, 2482, of), (2566, 2576, sf), (2583, 2600, 'ORG'),
        (2729, 2750, of), (2771, 2775, 'CARDINAL'), (2786, 2792, 'ORG'), (2795, 2815, 'ORG'), (2863, 2866, 'CARDINAL'),
        (3024, 3029, ql), (3162, 3174, 'CARDINAL'), (3275, 3284, 'DATE'), (3319, 3325, 'CARDINAL'), (3372, 3386, 'ORG'),

        (146, 148, cp), (772, 774, cp), (3006, 3008, cp), (227, 237, we), (344, 354, we),
        (297, 302, fw), (284, 293, fw), (407, 413, ol), (433, 439, pl), (569, 579, fw), (475, 482, ol), (620, 626, sv),
        (728, 748, pd), (595, 603, lb), (806, 815, se), (876, 885, ap), (973, 982, dv), (1039, 1049, we), (1089, 1094, pf),
        (1096, 1104, fw), (1106, 1113, fw), (1131, 1153, ap), (1154, 1165, tl), (1176, 1189, tl), (1322, 1332, we),
        (1746, 1753, ps), (1874, 1883, sf), (1940, 1954, ap), (68, 70, 'GPE'),
    ]}),
    (D8, {"entities": [
        (501, 514, 'ORG'), (2555, 2563, 'NORP'),

        (12, 36, ps), (45, 54, 'MONEY'), (65, 72, 'GPE'), (111, 135, ps), (151, 159, 'MONEY'), (204, 226, 'ORG'),
        (244, 268, ps), (287, 302, 'GPE'), (332, 355, of), (357, 365, sf),  (447, 469, cp), (609, 614, 'ORG'),
        (684, 687, pd), (727, 732, pl), (741, 763, se), (920, 942, se),  (765, 768, at), (839, 845, lb), (847, 857, pl),
        (859, 862, ol), (867, 871, ol), (906, 911, pl),(975, 979, 'ORG'),
        (1024, 1027, at), (1085, 1095, we), (1102, 1105, tl),
        (1177, 1182, ds), (1200, 1206, dv), (1232, 1246, ap), (1329, 1334, 'ORG'), (1811, 1829, 'DATE'), (1833, 1843, we),
        (1845, 1867, 'ORG'), (2460, 2464, 'GPE'), (2508, 2525, 'GPE'), (2607, 2613, 'GPE'),
        (2615, 2619, 'CARDINAL'), (2620, 2642, 'ORG'), (2647, 2664, of), (2743, 2749, 'PERSON'),

        (74, 76, 'GPE'), (676, 683, dv), (704, 725, pd), (734, 739, ap), (801, 806, fw), (1060, 1065, fw), (811, 824, fw),
        (1070, 1083, fw), (833, 837, at), (913, 918, ap),  (945, 970, dt), (792, 799, fw),  (1051, 1058, fw), (370, 391, ge),
    ]}),
    (D9, {"entities": [
        (25, 31, pl), (33, 41, ds), (43, 50, tl), (52, 58, pf), (97, 120, ps),
        (240, 246, dv), (290, 303, of), (309, 329, of), (410, 425, ps), (427, 445, ps), (461, 478, ps), (580, 592, dv),
        (611, 626, ps), (763, 781, se), (895, 901, pl), (912, 918, fw),
        (921, 927, pf), (941, 949, ds), (1260, 1265, 'DATE'), (1312, 1316, 'GPE'),
        (1392, 1409, 'GPE'), (1448, 1455, 'ORG'), (1850, 1867, of), (2225, 2242, 'GPE'), (2343, 2354, 'DATE'), (2357, 2368, 'ORG'),

        (60, 65, fw), (904, 909, fw), (67, 75, dt), (930, 938, dt), (77, 83, dt), (227, 239, at), (266, 282, of),
        (530, 538, dv), (630, 641, se), (696, 738, ql), (786, 797, ql), (1206, 1229, ps), (126, 136, we), (1235, 1245, we),
    ]}),
    (D10, {"entities": [
        (8, 31, ps), (212, 236, ps), (288, 307, ps), (363, 376, ql), (397, 406, ps), (588, 592, pt),
        (733, 752, ps), (816, 822, dv), (1015, 1018, pd), (1019, 1036, se), (1134, 1137, ol),
        (1153, 1161, dv), (1242, 1252, tm), (1346, 1354, 'DATE'), (1355, 1365, we), (1379, 1382, pd), (1395, 1403, 'DATE'),
        (1407, 1417, we), (1528, 1532, ol), (1534, 1538, pl), (1540, 1543, pl), (1545, 1551, pl),
        (1559, 1563, pl), (1589, 1598, at), (1603, 1618, se), (1624, 1627, tl), (1651, 1654, at),
        (1674, 1680, fw), (1682, 1687, fw), (1689, 1696, fw), (1698, 1703, 'GPE'),
        (1746, 1758, at), (1777, 1780, pt), (1804, 1817, se), (1840, 1842, dv), (1843, 1845, dv), (1914, 1936, ge),
        (1996, 2000, 'GPE'), (2004, 2024, cs), (2026, 2029, pd), (2043, 2059, cs), (2130, 2149, pd),
        (2169, 2174, pl), (2178, 2185, os_), (2221, 2224, pf), (2226, 2241, pf),
        (2243, 2255, pf), (2274, 2286, ap), (2325, 2332, tl),

        (114, 121, dv), (144, 151, pd), (1223, 1230, pd), (313, 324, dv), (1254, 1275, tm), (1465, 1484, at),
        (1485, 1495, we), (1553, 1555, pl), (1564, 1574, we), (1628, 1638, we), (1705, 1710, fw), (1715, 1722, fw),
        (1828, 1835, cs), (2063, 2084, we), (2156, 2167, pl), (2186, 2196, we), (2202, 2219, pf), (2257, 2267, we),
        (2309, 2319, we), (2292, 2308, os_),
    ]})
]

if __name__ == '__main__':
    word = "object-oriented design"

    print_entities(TRAIN_DATA)

    entity_finder(word, D8)
