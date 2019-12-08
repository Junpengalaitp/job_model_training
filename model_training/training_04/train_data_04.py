from model_training_algo.constants import pl, lb, cs, pt, ds, dv, we, os_, ap, pf, cp
from model_training.training_04.job_desc_04 import *

TRAIN_DATA = [
    (D1, {'entities': [(660, 667, dv), (1721, 1763, we), (1815, 1837, ap), (1850, 1865, cs), (1874, 1884, cs), (1980, 1984, lb),
                       (1986, 1999, lb), (2001, 2007, lb), (2012, 2016, lb), (2045, 2053, lb), (2087, 2090, pf)]}),
    (D2, {'entities': [(155, 173, dv), (270, 278, lb), (1311, 1319, lb), (2659, 2667, lb), (283, 290, lb), (1324, 1331, lb),
                       (2671, 2678, lb), (1565, 1570, pl), (1891, 1897, pl), (1899, 1905, lb), (2351, 2356, ap), (2586, 2591, lb),
                       (2592, 2597, lb)]}),
    (D3, {'entities': [(32, 51, dv), (200, 203, pt), (281, 284, pt), (667, 670, pt), (169, 174, lb), (1008, 1013, lb),
                       (1226, 1231, lb), (1015, 1025, pl), (1141, 1151, pl), (1027, 1033, pl), (1036, 1040, pl), (1088, 1093, lb),
                       (1233, 1238, lb), (1094, 1100, lb), (1102, 1108, pl), (1133, 1139, pl), (1153, 1155, pl), (1171, 1176, ds),
                       (1182, 1187, pf), (1202, 1208, pf), (1240, 1246, lb)]}),
    (D4, {'entities': [(2131, 2168, we), (2203, 2208, ds), (2210, 2218, ds), (2220, 2225, ds), (2227, 2233, ds), (2235, 2248, lb),
                       (2423, 2436, ap), (2677, 2683, pl), (2684, 2690, lb), (2692, 2696, pl), (2697, 2702, lb),
                       (1231, 1237, pl), (1436, 1442, pl), (2186, 2192, pl), (2704, 2710, pl), (2711, 2718, ds),
                       (2735, 2738, ap), (2746, 2749, ap), (2805, 2812, pl)]}),
    (D5, {'entities': [(1458, 1461, pt), (1134, 1140, pl), (1168, 1174, pl), (1480, 1486, pl), (3018, 3024, pl), (3374, 3380, pl),
                       (1489, 1495, lb), (3579, 3585, lb), (1512, 1517, ap), (3588, 3593, lb), (3295, 3298, pf), (3311, 3367, we)]}),
    (D6, {'entities': [(141, 151, cs), (437, 447, cs), (832, 842, cs), (2747, 2757, cs), (190, 197, dv), (393, 400, dv),
                       (2799, 2801, pl), (2995, 2997, pl), (3059, 3061, pl), (2812, 2814, pl), (2824, 2827, pl), (2879, 2885, pl),
                       (2887, 2893, lb), (2786, 2790, lb), (2895, 2901, lb), (2915, 2920, lb), (2922, 2932, ds),
                       (2934, 2939, ds), (2944, 2952, lb)]}),
    (D7, {'entities': [(1382, 1385, pf), (1975, 1978, pf), (1762, 1767, os_), (1784, 1790, os_), (1791, 1797, os_), (1799, 1805, os_),
                       (1806, 1812, os_), (1837, 1846, pt), (1848, 1855, cp), (1857, 1866, cp), (1898, 1903, ds), (1905, 1911, ds),
                       (1913, 1923, ds), (1925, 1931, ds), (1390, 1395, pf), (1980, 1985, pf), (1479, 1488, pf), (1987, 1996, pf),
                       (1468, 1474, pf), (1998, 2004, pf)]}),
    (D8, {'entities': [(21, 30, dv), (32, 41, dv), (1489, 1498, dv), (47, 63, dv), (264, 284, dv), (343, 362, dv),
                       (1552, 1562, pl), (1587, 1597, pl), (1864, 1874, pl), (1602, 1607, lb), (1678, 1683, lb),
                       (1685, 1697, lb), (1876, 1882, pl), (1884, 1890, pl), (1892, 1896, pl), (1916, 1923, pl),
                       (1925, 1929, ds), (1945, 1952, lb), (1954, 1961, lb), (1963, 1970, ds), (1972, 1982, pt),
                       (2011, 2017, pf), (2040, 2043, ds), (2045, 2050, ds), (2052, 2060, ds), (2062, 2067, ds),
                       (2099, 2102, pf), (2104, 2125, pf)]}),
    (D9, {'entities': [(2101, 2107, pf), (2126, 2133, lb), (2134, 2136, ap), (2138, 2141, pf), (2143, 2149, pf), (3011, 3017, pf),
                       (2411, 2416, lb), (2763, 2768, lb), (2402, 2409, lb), (2418, 2421, lb), (2779, 2788, lb), (2665, 2670, lb),
                       (2672, 2677, lb), (2679, 2682, pl), (2684, 2690, lb), (2692, 2698, lb), (2700, 2707, lb), (2754, 2761, lb),
                       (2709, 2714, pl), (2721, 2725, pl), (2727, 2731, lb), (2770, 2773, lb), (2716, 2719, pl), (2793, 2796, pl),
                       (2926, 2930, ds), (2932, 2936, pt), (2938, 2941, pt), (2979, 2987, dv),
                       (3775, 3783, dv), (2841, 2855, dv), (2998, 3004, lb), (3006, 3009, lb),
                       (3069, 3079, pl), (3092, 3112, we), (3382, 3391, dv), (3661, 3665, pl), (3667, 3673, pl),
                       (3675, 3679, pl), (3685, 3705, dv), (3902, 3911, lb), (3886, 3900, pf)]}),
    (D10, {'entities': [(47, 76, dv), (1444, 1454, pl), (119, 123, pl), (660, 664, pl), (1090, 1094, pl), (1175, 1179, pl),
                        (1224, 1228, pl), (1432, 1436, pl), (112, 118, lb), (1095, 1101, lb), (1339, 1344, lb),
                        (1247, 1253, lb), (1255, 1260, lb), (1192, 1203, lb), (1345, 1348, ap), (1481, 1489, lb)]})
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