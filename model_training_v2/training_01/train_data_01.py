from collections import defaultdict

from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_v2.training_01.job_desc_01 import \
    _2923a7d6b1cf9df5993253768bb05ada370ce5e55d1772acf94bbcd41fac2e85 as D1, \
    _e513f83c20942b5ecaa3a1247c154892802845c5eb3161201f4c0394d419a427 as D2, \
    _c213b25d1182cce917971584991d1aef747d677967eb2dfc490ad45543554d1a as D3, \
    _ae5f6f5c56847e54f10a1a6ba2fa3420744e630f7e6ce76c1f60bf3b4f128ce9 as D4, \
    _9cb6da0cffb3173ef81c4fa03e3beda44459c5c0bf616acf3a043aaa9cba2329 as D5, \
    _30ca4245355909d1dc9f89809c4d7158d6dce8c5f8ff36da555320db3aa80aff as D6, \
    _516a36ab2091b8e70b7c6f638f1830cd0cf49a5e1d4ea93fc6c8b4840d678010 as D7, \
    _1dd6b08b6221b5ebebcf086304b3f2c846eae4a71d833d26d53b250955de811a as D8, \
    _ec4eec423b2b46859324e6f8df6bc44f635d51415a224fc13b36b9eacdf5c223 as D9, \
    _ab44ba20db20d123646df89f89464e37995859d5cbf49b825b86ef32de354dc9 as D10

TRAIN_DATA = [
    (D1, {
        "entities": [(17, 41, ps), (318, 328, pl), (346, 352, pl), (354, 360, pl), (405, 410, ds), (440, 443, pf),
                     (881, 884, pf), (365, 369, pl), (450, 458, ds), (476, 485, ds), (470, 474, ds), (487, 495, dv),
                     (552, 559, se), (516, 540, ql), (561, 566, fw), (568, 571, tl), (573, 577, fw), (671, 678, se),
                     (680, 685, ds), (707, 720, lb), (754, 766, at), (768, 775, ol), (873, 876, pf), (817, 825, dv),
                     (853, 867, pf), (983, 993, se), (895, 901, pf), (906, 928, ap), (943, 952, se), (954, 963, se),
                     (1030, 1046, ps), (1156, 1163, dv), (1595, 1602, dv), (2433, 2440, dv), (1328, 1338, se),
                     (1224, 1234, se), (1239, 1246, se), (1372, 1382, at), (1383, 1396, at),
                     (1398, 1417, se), (1422, 1435, se), (1979, 1992, se), (2292, 2308, ps), (1816, 1835, sf),
                     (1994, 2004, sf), (2009, 2019, sf), (2055, 2075, sf), (2083, 2098, sf),
                     (2120, 2150, ge), (2163, 2185, ge), (2376, 2397, sf), (2540, 2557, ql),
                     (2574, 2587, ge), ]}),
    (D2, {"entities": [(257, 267, ge), (790, 819, ps),
                       (946, 950, pd), (4167, 4171, pd), (619, 626, cp), (998, 1003, ap), (1543, 1545, dv),
                       (3619, 3622, dv),
                       (4741, 4743, dv), (2416, 2438, ap), (2446, 2448, dv), (2450, 2458, dv), (2460, 2484, se),
                       (3344, 3353, se),
                       (2489, 2496, se), (3015, 3026, se), (3075, 3091, cs), (3113, 3163, we), (3181, 3196, pd),
                       (3638, 3648, pl), (3515, 3519, pl), (4570, 4574, pl),
                       (3535, 3538, ol), (3574, 3579, os_), (3629, 3633, ol), (3634, 3637, ol), (3667, 3677, pl),
                       (3712, 3722, pl),
                       (4759, 4769, pl), (3733, 3739, lb), (3757, 3780, pd), (3797, 3802, fw), (3807, 3814, fw),
                       (3903, 3907, pt),
                       (3912, 3915, ol), (3948, 3951, tl), (3953, 3967, se), (3969, 3977, tl), (3999, 4015, ap),
                       (3859, 3871, se), (4347, 4359, se), (4507, 4514, at), (4515, 4519, dt), (4520, 4523, pt),
                       (4580, 4585, sv),
                       (4591, 4598, sv), (4603, 4615, cs), (4646, 4651, ds), (4658, 4665, fw), (4674, 4679, ds),
                       (4684, 4691, se),
                       (4719, 4735, se), (4770, 4773, at), (4813, 4833, se), (4843, 4862, se), (5001, 5004, pf),
                       (5025, 5031, pf),
                       (5042, 5048, tl), (5050, 5055, tl), (5057, 5061, fw), (5063, 5068, lb), (5070, 5076, tl),
                       (5078, 5091, tl),
                       (5093, 5108, tl), (3412, 3425, ql)]}),
    (D3, {"entities": [(74, 82, pd), (89, 94, ap), (161, 168, se), (170, 183, se), (185, 195, se), (197, 208, se),
                       (234, 241, se), (2015, 2022, se), (381, 390, se), (418, 421, pt), (895, 899, pt),
                       (1722, 1725, pt), (666, 715, we), (746, 750, ol), (751, 754, pl), (1864, 1867, pl),
                       (758, 761, ol), (778, 785, fw), (787, 792, fw), (794, 801, lb), (803, 807, ol), (823, 835, pd),
                       (856, 860, pt), (923, 927, pt), (909, 913, dt), (919, 922, ol), (946, 953, se), (970, 979, ds),
                       (981, 988, ds), (990, 993, sv), (1080, 1094, se), (1110, 1117, ap), (1159, 1165, pf),
                       (1238, 1258, ge),
                       (1291, 1301, sf), (1302, 1309, se), (1477, 1484, ge), (1311, 1325, se), (1331, 1339, sf),
                       (1397, 1406, ge), (1558, 1570, ap), (1575, 1586, ap),
                       (1613, 1620, fw), (1622, 1627, fw), (1629, 1641, pf), (1643, 1651, fw),
                       (1665, 1672, fw), (1842, 1857, pd),
                       (2151, 2179, of), (2069, 2074, tl), (2079, 2084, tl)]}),
    (D4, {"entities": [(395, 399, fw), (883, 887, fw), (354, 377, pd), (423, 448, we), (776, 810, we),
                       (832, 861, pd), (889, 892, at), (894, 904, pl), (915, 935, sf), (997, 1002, lb),
                       (1004, 1015, lb),
                       (1031, 1043, dv), (1135, 1159, of), (1207, 1228, of), (1576, 1586, sf),
                       (2000, 2013, ge), (2060, 2074, ge)]}),
    (D5, {"entities": [(73, 87, cp), (788, 802, cp),  (244, 263, we), (289, 298, ps), (0, 6, pl), (494, 500, pl),
                       (518, 525, lb), (530, 536, lb), (553, 556, pf), (557, 579, pd), (593, 601, pf), (603, 609, pf),
                       (611, 619, ds), (621, 623, pf), (683, 695, pf), (803, 807, pt), (824, 830, sv), (835, 842, lb),
                       (849, 865, pd), (882, 889, tl), (894, 900, pl), (1018, 1025, ol), (969, 980, se),
                       (1152, 1170, ai),
                       (1107, 1117, cs), (1137, 1147, cs), (1826, 1848, tm),
                       (1352, 1382, ge), (1753, 1766, sf), (1874, 1883, of), (1985, 2010, of), (1960, 1980, of),
                       ]}),
    (D6, {"entities": [(337, 351, pd), (395, 417, sf), (887, 890, pl), (921, 924, pl), (2812, 2815, pl),
                       (1005, 1014, tl), (1059, 1068, tl), (1143, 1146, pl), (1173, 1178, lb), (1192, 1196, sv),
                       (1230, 1237, tl), (1277, 1297, ge), (1524, 1540, pd), (1900, 1909, se), (1911, 1918, se),
                       (1940, 1951, ap), (2003, 2008, ap), (2059, 2064, ap), (2212, 2232, sf),
                       (2311, 2322, sf), (3249, 3255, of), (3281, 3295, of), (3308, 3325, of), (3757, 3774, of),
                       (3361, 3373, of), (3378, 3399, of), (3840, 3857, of)]}),
    (D7, {"entities": [(56, 61, cp), (955, 969, ps), (1201, 1207, pl), (2331, 2337, pl), (2358, 2365, pl),
                       (1253, 1260, pl), (2382, 2389, pl), (1262, 1266, pl), (2374, 2378, pl), (1268, 1269, pl),
                       (1275, 1278, pl), (1366, 1376, ds), (2554, 2564, ds), (1378, 1383, ds), (2544, 2549, ds),
                       (1385, 1392, ds), (1394, 1402, pf), (2534, 2542, pf), (1408, 1413, ds),
                       (1484, 1492, dt), (1506, 1519, ps), (1546, 1555, se), (2822, 2831, se), (1567, 1574, se),
                       (1580, 1591, se), (1647, 1651, pt), (1625, 1641, pd), (1596, 1610, pd), (1676, 1705, tm),
                       (1737, 1745, ps), (1749, 1763, ps), (1771, 1786, ps), (1867, 1873, ap),
                       (1973, 1993, se), (2014, 2026, se), (2118, 2124, sf), (2898, 2907, sf), (2912, 2920, sf),
                       (2948, 2955, ge), (2960, 2970, ge), (2399, 2402, pl), (2659, 2668, at), (2670, 2675, dt),
                       (1474, 1479, dt), (2188, 2198, ge), (2733, 2743, ge), (2706, 2726, sf), ]}),
    (D8, {"entities": [(638, 645, ge), (650, 665, ge), (976, 981, lb), (983, 995, fw), (1004, 1014, pl),
                       (1041, 1044, os_), (1049, 1056, os_), (1226, 1237, pd),
                       (1278, 1285, ge), (1491, 1497, cp), (1523, 1530, cp), (240, 247, of),
                       (1396, 1401, cp), (1945, 1960, of), (2069, 2080, pd), (2128, 2142, of),
                       (1365, 1385, of), (1458, 1467, cp), (2431, 2442, sf), (2212, 2221, sf), ]}),
    (D9, {"entities": [(240, 247, of), (804, 824, of), (1946, 1966, of),
                       (960, 982, we), (1029, 1036, os_), (1110, 1117, os_), (1065, 1071, pl), (1088, 1093, pf),
                       (1118, 1130, ap), (1147, 1151, dt), (1153, 1156, ol), (1158, 1162, pt), (1164, 1168, at),
                       (1211, 1215, pl), (1217, 1223, sv), (1225, 1228, pl), (1246, 1257, pf), (1305, 1322, se),
                       (1327, 1351, se), (1782, 1800, of),
                       (1462, 1473, pd), (1514, 1521, ge), (1601, 1621, of), (1632, 1637, cp),
                       (1694, 1703, cp), (1727, 1733, cp), (1759, 1766, cp), (2181, 2196, of), (2305, 2316, pd),
                       (2364, 2378, of), (2448, 2457, sf), (2667, 2678, sf)]}),
    (D10, {"entities": [(406, 421, ps), (485, 493, pd), (2098, 2106, pd), (586, 594, se), (574, 581, se), (973, 983, ge),
                        (988, 999, ge), (1071, 1089, sf), (1141, 1148, ge),
                        (1494, 1507, sf), (2163, 2181, at), (2211, 2220, tl), (5003, 5012, tl),
                        (2297, 2305, at), (2369, 2376, se), (2420, 2425, ol), (2427, 2431, ol), (2433, 2443, pl),
                        (2485, 2495, pl), (2444, 2450, lb), (2456, 2459, pl), (2516, 2523, fw), (2527, 2532, lb),
                        (2557, 2572, se), (2590, 2593, tl), (2623, 2654, we), (2916, 2921, dv), (2985, 2994, tl),
                        (3470, 3491, of), (3493, 3497, of), (3524, 3540, of), (3542, 3555, of),
                        (3561, 3576, of), (3857, 3874, of), (4660, 4666, tl), (4671, 4677, tl), ]})
]

if __name__ == '__main__':
    print_entities(TRAIN_DATA)

    entity_finder('crypto', D8)
