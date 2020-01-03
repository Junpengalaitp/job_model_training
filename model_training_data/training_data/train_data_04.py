from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, ai, cp
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_data.training_text.job_desc_04 import \
    _c6f44693fae1e286a76031c7b39223963a709aa5769e4a4e7ac72481111a1357 as D1, \
    _aa17369586948f3637b7dda8a9db905133c9123bccb70bc781a804e8849c0081 as D2, \
    _bf4a694f7eef157a4208469309d91388cd253e7f93b3c747150e1f696575f99f as D3, \
    _88d8d77d0462d6fb35c8a965642b727e2a1c9d05e01aaa462d75e21ecdd54b70 as D4, \
    _7492fc8afd72c14ad860b79a77961c9b6eb9ba3414a70715442959bc013393ff as D5, \
    _7c7a2be0ff41ee168cd4fdc9a4d8dfb8470d8f504f8bee8a5e5d0fe834898075 as D6, \
    _8b8db05b3c7bd1801a35d79b6c5a78ba3aab2e0a08c0d5caa2f8e2568672462b as D7, \
    _23caffb33a533a774389398a3064b1831286a520fbc2471749c9e8a1a62fa2e8 as D8, \
    _360af1b1ad05eb913aa7d8328e3a4b8d1ae26c2c2453e045725eb1e6c09bdc4e as D9, \
    _020dd7c157022a1bd8b9722e20cb922cf60dca2489ed28788e0ca63a7bc9ad3c as D10

TRAIN_DATA = [
    (D1, {"entities": [(95, 100, 'MONEY'), (1224, 1235, 'GPE'), (1442, 1453, 'FAC'), (1931, 1936, 'DATE'),
                       (2485, 2496, 'FAC'), (2625, 2636, 'DATE'), (3395, 3405, 'CARDINAL'),  (3430, 3443, 'GPE'),
                       (3586, 3597, 'GPE'), (3720, 3729, 'TIME'), (3758, 3769, 'PERSON'), (3884, 3890, 'TIME'),
                       (3962, 3971, 'TIME'), (4016, 4029, 'DATE'),
                       (156, 167, ap), (181, 191, pd), (273, 281, cp), (286, 303, cp), (561, 575, cp), (590, 596, cp),
                       (946, 963, tm), (1020, 1037, of), (1460, 1468, dv), (1470, 1477, dv), (1479, 1489, dv),
                       (1491, 1498, dv), (1500, 1516, dv), (1619, 1627, dv), (1629, 1639, pl), (1641, 1646, lb),
                       (1648, 1652, lb), (1654, 1658, ol), (1678, 1682, pt), (1683, 1690, dv), (1692, 1694, pl),
                       (1696, 1703, ol), (1705, 1715, ds), (1717, 1722, ds), (1750, 1760, pf),
                       (1762, 1768, pf), (1770, 1791, pf), (1793, 1802, tl), (4338, 4341, ps), (4342, 4345, ps), ]}),
    (D2, {"entities": [(16, 26, 'ORG'), (91, 108, 'CARDINAL'), (329, 339, 'ORG'), (388, 398, 'ORG'), (409, 410, 'CARDINAL'),
                       (465, 485, 'CARDINAL'), (903, 913, 'ORG'), (1321, 1331, 'ORG'), (1364, 1368, 'CARDINAL'),
                       (1406, 1413, 'GPE'), (1455, 1464, 'DATE'), (1604, 1614, 'ORG'), (1635, 1653, 'DATE'),
                       (1815, 1831, 'DATE'), (2316, 2323, 'LANGUAGE'), (2522, 2526, 'CARDINAL'), (2542, 2549, 'GPE'),
                       (2551, 2560, 'GPE'), (2575, 2579, 'CARDINAL'), (2712, 2719, 'GPE'), (2763, 2773, 'PERSON'),
                       (2799, 2811, 'DATE'), (2955, 2966, 'ORG'), (3031, 3033, 'ORG'),  (3136, 3146, 'ORG'),
                       (3446, 3454, 'ORG'),  (3456, 3463, 'ORG'),  (3465, 3473, 'ORG'), (3664, 3674, 'ORG'),
                       (57, 72, cp), (713, 716, pl), (718, 725, fw), (727, 732, ds), (1935, 1940, ds), (734, 739, ds),
                       (1955, 1960, ds), (741, 754, lb), (767, 774, ap), (798, 804, pf), (1125, 1128, pd),
                       (1565, 1572, cp), (1663, 1681, cp), (1741, 1757, tm),
                       (1979, 1982, pt), (2036, 2048, ge), (2067, 2076, ql), (2088, 2109, ge), (2140, 2163, ge),
                       (2177, 2196, ge), (2292, 2312, sf), (2406, 2416, pl), (2443, 2461, of),
                       (2496, 2516, tm), ]}),
    (D3, {"entities": [(505, 513, 'DATE'), (593, 595, 'GPE'), (603, 610, 'GPE'), (1070, 1078, 'DATE'), (1779, 1785, 'CARDINAL'),
                       (2071, 2076, 'ORG'),
                       (246, 260, ps), (325, 332, dv), (517, 527, we), (626, 639, ps), (1014, 1030, ai), (1307, 1323, ai),
                       (1905, 1921, ai), (1082, 1104, we),  (59, 71, cp), (729, 741, cp), (1247, 1255, sv), (1525, 1531, fw),
                       (1535, 1540, fw), (1757, 1765, ai), (1771, 1778, se), (1957, 1960, ai),
                       (1975, 1991, lb), (1993, 2000, lb), (2009, 2015, pl), (2018, 2022, lb),
                       (1481, 1497, pd), (2102, 2118, pd), (835, 844, ai), (2119, 2128, ai), (2176, 2187, pf),
                       (2191, 2199, tl), ]}),
    (D4, {"entities": [(1330, 1350, 'ORG'), (1860, 1869, 'DATE'), (1894, 1913, 'DATE'),
                       (20, 39, ps), (129, 143, se), (220, 229, tl), (1170, 1179, tl), (697, 710, ql), (1010, 1014, ol),
                       (776, 781, dv), (751, 772, se), (808, 821, ql), (1000, 1005, ol), (1039, 1049, pl),
                       (1050, 1056, lb), (1118, 1127, lb), (1434, 1449, se), (2301, 2307, pf), ]}),
    (D5, {"entities": [(2632, 2642, 'PERSON'), (2646, 2655, 'GPE'), (2678, 2681, 'CARDINAL'),
                       (2685, 2688, 'CARDINAL'), (3233, 3242, 'GPE'), (3291, 3293, 'ORG'),
                       (48, 63, ps), (175, 181, dv), (68, 86, ps), (384, 394, cp), (512, 515, fw), (517, 524, sv),
                       (526, 531, lb), (536, 544, fw), (924, 927, pf), (951, 971, se), (973, 994, se), (1302, 1315, fw),
                       (1317, 1325, ds), (1330, 1335, ds), (1344, 1353, dv), (1379, 1386, fw), (1388, 1400, pl),
                       (1405, 1411, lb), (1413, 1425, lb), (1427, 1433, sv), (1438, 1447, lb), (1521, 1533, cs),
                       (1673, 1678, tl), (1680, 1695, tl), (1717, 1721, tl), (1747, 1760, sf), (1796, 1801, os_),
                       (1865, 1876, pd), (1909, 1921, at), (1922, 1928, dv), (1934, 1955, ap), (1983, 1996, pf),
                       (1998, 2020, ap), (2022, 2039, ap), (2041, 2058, ql), (2075, 2097, se), (2112, 2115, tl),
                       (2157, 2166, tl), (2168, 2175, tl), (2331, 2350, pf), (2392, 2395, pf), (2299, 2302, pf),
                       (2397, 2400, pf), (2433, 2440, pf), (2442, 2448, pf), (2450, 2460, pf), (2462, 2464, pf),
                       (2466, 2469, pf), (2471, 2474, pf), (2570, 2590, sf), (2286, 2289, os_), (2277, 2284, tl),
                       (2307, 2313, pf), (2177, 2183, tl), ]}),
    (D6, {"entities": [(122, 127, 'ORDINAL'), (2411, 2415, 'PERCENT'), (2438, 2441, 'PERCENT'), (2654, 2660, 'DATE'),
                       (12, 17, lb), (467, 472, lb), (720, 725, lb), (828, 833, lb), (950, 955, lb), (1451, 1456, lb),
                       (36, 43, cp), (788, 791, ps), (1130, 1170, tm), (1206, 1222, ql), (1233, 1249, pd),
                       (877, 903, dv), (1615, 1641, dv), (1643, 1649, dv), (1730, 1733, pf), (1795, 1800, os_),
                       (1802, 1812, pf), (1818, 1824, pf), (1849, 1859, cs), (1899, 1907, cs), (2060, 2074, ql),
                       (2013, 2033, ql), (2116, 2131, pd), (2157, 2163, fw), (2165, 2169, sv), (2171, 2179, ds),
                       (2237, 2246, dv), (2274, 2279, lb), (2374, 2392, of), (2393, 2409, of), (2474, 2492, of),
                       (2493, 2497, of), (2498, 2522, of), (2529, 2545, of), (2554, 2560, of), (2633, 2653, tm),
                       (2674, 2693, of), ]}),
    (D7, {"entities": [(16, 19, 'CARDINAL'), (23, 33, 'ORG'), (1667, 1677, 'ORG'), (1869, 1873, 'PERSON'),
                       (1876, 1882, 'PERSON'), (1885, 1890, 'PERSON'), (1892, 1918, 'PERSON'), (1987, 1995, 'DATE'),
                       (2526, 2533, 'LANGUAGE'), (2655, 2659, 'PERSON'), (2883, 2893, 'ORG'), (3320, 3324, 'GPE'),
                       (87, 99, se), (233, 245, se), (319, 331, se), (445, 457, se), (559, 571, se), (799, 811, se),
                       (935, 947, se), (1654, 1666, se), (1739, 1751, se), (363, 380, ps),
                       (2499, 2516, ps), (525, 531, dv), (2802, 2808, dv), (589, 607, ps), (105, 133, pd),
                       (970, 988, ps), (634, 652, dv), (1357, 1375, dv), (615, 628, sf), (742, 761, tm),
                       (1090, 1099, se), (1113, 1122, se), (1137, 1141, pl), (2047, 2051, pl), (1144, 1146, pl),
                       (2056, 2058, pl), (2060, 2062, pl), (1155, 1174, ap), (1201, 1213, ap), (1294, 1323, ap),
                       (1511, 1521, se), (2121, 2135, se), (2180, 2204, cs), (1999, 2009, we),
                       (2220, 2231, se), (2321, 2330, at), (2367, 2370, tl), (2372, 2378, pf), (2380, 2384, ol),
                       (2397, 2407, cp), (3188, 3205, of), (3228, 3250, of), ]}),
    (D8, {"entities": [(40, 61, 'ORG'), (886, 906, 'CARDINAL'), (1224, 1231, 'ORG'), (1553, 1558, 'PRODUCT'),
                       (2152, 2161, 'ORG'), (2420, 2425, 'ORG'), (1967, 1975, 'DATE'),
                       (0, 6, tl), (200, 206, tl), (341, 347, tl), (455, 461, tl), (560, 566, tl), (722, 728, tl),
                       (1241, 1247, tl), (1322, 1328, tl), (283, 299, ai), (1671, 1687, ai), (2036, 2052, ai),
                       (2092, 2108, ai), (420, 435, cp), (1163, 1190, ai), (1429, 1443, pd), (1534, 1552, ql),
                       (2083, 2091, ai), (1976, 1995, we), ]}),
    (D9, {"entities": [(261, 274, 'DATE'), (283, 288, 'ORDINAL'), (289, 298, 'CARDINAL'), (349, 364, 'DATE'),
                       (380, 386, 'ORDINAL'), (401, 417, 'DATE'), (426, 435, 'CARDINAL'), (472, 482, 'CARDINAL'),
                       (483, 491, 'NORP'), (1176, 1192, 'PERSON'), (1209, 1216, 'CARDINAL'), (1265, 1273, 'CARDINAL'),
                       (1334, 1343, 'CARDINAL'), (1717, 1731, 'LOC'), (1508, 1546, 'ORG'), (2459, 2489, 'WORK_OF_ART'),
                       (2493, 2521, 'WORK_OF_ART'), (2525, 2552, 'WORK_OF_ART'), (2560, 2577, 'WORK_OF_ART'),
                       (3126, 3134, 'ORG'), (3136, 3142, 'ORG'), (3590, 3598, 'WORK_OF_ART'), (4072, 4088, 'DATE'),
                       (4548, 4554, 'DATE'), (4633, 4637, 'DATE'), (4874, 4882, 'NORP'), (4886, 4900, 'NORP'),
                       (4, 15, cp), (1629, 1640, cp), (1845, 1856, cp), (2755, 2766, cp), (221, 226, cp), (299, 304, cp),
                       (451, 456, cp), (665, 670, cp), (1110, 1115, cp), (1243, 1248, cp), (1277, 1282, cp),
                       (1935, 1940, cp), (2281, 2286, cp), (3552, 3557, cp), (4349, 4354, cp), (4449, 4454, cp),
                       (5191, 5196, cp), (521, 537, cp), (1737, 1745, cp), (2892, 2914, sf), (2847, 2861, ge),
                       (3014, 3018, at), (3036, 3039, pf), (3148, 3151, pf), (3045, 3048, pl), (3041, 3044, cs),
                       (3050, 3052, ap), (3064, 3069, ds), (3079, 3082, ol), (3094, 3097, pt), (3112, 3118, tl),
                       (3162, 3165, pf), (3167, 3170, pf), (3172, 3174, pf), (3176, 3186, pf), (3188, 3195, pf),
                       (3202, 3207, os_), (3274, 3277, pd), (3321, 3324, pd), (3788, 3791, pd), (3286, 3290, ol),
                       (3292, 3295, ol), (3340, 3342, pl), (3374, 3401, ql), (3451, 3477, ql), (3495, 3498, tl),
                       (4258, 4267, dv), (4555, 4560, ap), (4679, 4693, ps), (4699, 4721, ps), (4785, 4803, of),
                       (4850, 4868, of)]}),
    (D10, {"entities": [(744, 745, 'CARDINAL'), (1848, 1869, 'ORG'), (2000, 2012, 'ORG'),
                        (61, 79, ps), (189, 207, ps), (148, 156, dv), (318, 337, ql), (420, 443, of), (520, 526, pd),
                        (683, 689, pd), (997, 1007, pd), (1372, 1378, pd), (573, 588, ap), (597, 600, os_),
                        (993, 996, os_), (728, 731, pl), (736, 743, fw), (746, 752, pf), (753, 758, ds), (855, 860, ds),
                        (759, 764, ds), (765, 773, ds), (774, 777, pf), (1446, 1449, pf), (779, 782, pf), (784, 787, pf),
                        (826, 840, pd), (891, 903, at), (938, 954, cs), (1034, 1053, se), (1067, 1070, tl),
                        (1118, 1139, ql), (1418, 1437, pf), (1532, 1544, at), (1673, 1677, ol), (1679, 1690, lb),
                        (1692, 1699, fw), (1744, 1758, ql), (1784, 1789, ap), (1794, 1799, ap), (1819, 1847, ge),
                        (1879, 1895, of), (1903, 1915, of), (1916, 1927, tm), ]}),
]

if __name__ == '__main__':
    word = "industry experience"

    print_entities(TRAIN_DATA)

    entity_finder(word, D8)