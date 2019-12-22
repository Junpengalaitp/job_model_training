import re

from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_02.job_desc_02 import \
    _45f21e8cc59d13ba57e5ad2f0366fac7093672f223b8e7c119b45e16d4dc0f6c as D1, \
    _696f54ea324f765d42525299d7bca0765be6aca0ec16fa84d01585cfec12bb9c as D2, \
    _3311541b9f01452f59eaee98039f4a82140e1b41d75da6dfd90f7ffc55051b24 as D3, \
    _309ce74603f4d3a7e222fa9785a6f5e0d1670d1c3dda1dbb3826d6148437b734 as D4, \
    _e0eb1c1637e0227bca225beea9405cd47f16fd161c393a64754e1b60d3c7bf59 as D5, \
    _fba8599e36e5fb7181f122265858b92d708a32233ca6c47177254a3fe6e4a431 as D6, \
    _a27147c87413de7fd486418b9f291ea93a5234b68e6c9a68a841b049678501c1 as D7, \
    _bb05ff489a277988a5c505d8bd105a13adec52e5bbe58e52d52d573f842d567a as D8, \
    _e69b49c4cb81ffe3749f3102d8cab6de3f1fb9dee0b30c98a4b5c39c2dd05994 as D9, \
    _ef4185606d7cb286d3e256864d93bcd6470e5a6059cc630a54f1b93bd3ba2d33 as D10

TRAIN_DATA = [
    (D1, {"entities": [(0, 18, ps), (71, 79, dv), (630, 638, dv), (1241, 1249, dv), (88, 103, ps), (129, 133, pd),
                       (188, 196, at), (290, 301, pd), (277, 289, pd),
                       (348, 355, pd), (755, 762, pd),  (456, 472, pd), (696, 712, pd), (616, 629, fw),
                       (991, 1004, fw), (1042, 1049, pd), (1155, 1165, ap), (1187, 1199, se), (1200, 1235, we),
                       (1337, 1353, ge), (1402, 1427, pd), (1499, 1503, at), (1504, 1508, dt),
                       (639, 642, pt), (1509, 1512, pt), (1559, 1563, pt), (1580, 1596, dv),
                       (1691, 1696, ap), (1727, 1748, ge), (1774, 1784, pl), (1804, 1811, fw), (1815, 1821, fw),
                       (1968, 1980, ge), (1982, 1996, sf), (2002, 2015, sf), (2070, 2094, ge),
                       (2279, 2295, of), (2327, 2344, of), (2453, 2469, tm),
                       (2479, 2497, of), (2532, 2547, of), (2569, 2575, of), (2788, 2794, pf), ]}),
    (D2, {"entities": [(28, 49, ps), (59, 61, pl), (1355, 1357, pl), (62, 66, fw), (144, 158, ps), (684, 688, fw),
                       (269, 287, of), (297, 315, of), (496, 506, pd), (731, 747, ai), (634, 665, ai),
                       (1061, 1076, of), (1176, 1196, sf), (1211, 1218, ge), (1241, 1271, pd), (1304, 1349, we),
                       (1405, 1418, we), (1419, 1428, fw), (1431, 1438, fw), (1451, 1457, dv), (1462, 1464, dv),
                       (1506, 1516, ap), (1530, 1552, we), (1553, 1559, pl), (1560, 1568, we), (1569, 1585, ai),
                       (1656, 1672, ai), (1639, 1655, ql), (1703, 1712, ai), (1789, 1800, se), (1802, 1813, se),
                       (1832, 1852, se), (1858, 1868, se), (1928, 1952, of), (2010, 2030, of), (2064, 2084, ap),
                       (2089, 2101, se), ]}),
    (D3, {"entities": [(204, 217, pd), (265, 285, tm), (424, 448, ps), (322, 348, pd), (461, 473, tm), (618, 647, pd),
                       (735, 741, pl), (967, 973, pl), (1721, 1727, pl), (743, 748, fw), (750, 755, ol), (757, 760, pl),
                       (762, 768, fw), (770, 774, ol), (776, 783, tl), (785, 790, ds), (792, 798, pf), (1840, 1846, pf),
                       (800, 803, pf), (1805, 1808, pf), (805, 814, tl), (816, 823, tl), (825, 834, ds), (836, 841, sv),
                       (843, 852, pf), (854, 860, pf), (862, 871, tl), (921, 930, of), (1996, 2005, of), (933, 940, ge),
                       (990, 1001, ql), (1003, 1014, ql),  (1035, 1050, ql), (1181, 1189, dv),
                       (1157, 1179, ap), (1191, 1208, se), (1210, 1213, ap), (1219, 1224, ap), (1259, 1280, se),
                       (1448, 1460, se), (1465, 1492, se), (1520, 1536, ps), (1551, 1569, se),
                       (1600, 1643, we), (1647, 1670, tm), (1741, 1748, sv), (1750, 1754, pl), (1756, 1760, pl),
                       (1762, 1764, pl), (1781, 1796, pf), (1810, 1813, pf), (1818, 1823, pf), (1848, 1860, ap),
                       (1862, 1872, at), (2102, 2124, tm), (2135, 2155, sf), (2159, 2170, sf), ]}),
    (D4, {"entities": [(58, 72, pd), (259, 266, pd), (406, 412, pd), (563, 576, tm), (859, 874, ap), (890, 898, dv),
                       (899, 906, se), (956, 958, pl), (1451, 1453, pl), (960, 966, pl), (1455, 1461, pl),
                       (972, 975, pl), (1467, 1470, pl), (996, 1011, ap), (1162, 1185, se), (1190, 1211, se),
                       (1275, 1277, dv), (1333, 1348, ap), (1471, 1493, we), (1501, 1517, pd), (1541, 1546, os_),
                       (1570, 1586, os_), (1604, 1623, pt), (1638, 1641, pt), (1651, 1655, pt), (1660, 1664, at),
                       (1666, 1676, pt), (1678, 1694, pt), (1712, 1729, pd), (1751, 1758, pd), (1807, 1814, pd),
                       (1845, 1862, ap), (1913, 1927, se), (1942, 1950, tl), (1955, 1959, tl), (2025, 2041, cs), ]}),
    (D5, {"entities": [(30, 52, pd), (53, 60, tm), (3412, 3419, tm), (3612, 3619, tm), (71, 90, ps), (128, 132, pd),
                       (3241, 3245, pd), (5192, 5196, pd), (137, 160, dv), (7, 9, dv), (169, 171, dv), (898, 900, dv),
                       (1180, 1182, dv), (2725, 2727, dv), (3120, 3122, dv), (3261, 3263, dv), (3348, 3350, dv),
                       (4896, 4898, dv), (4906, 4908, dv), (4951, 4953, dv), (5169, 5171, dv), (187, 231, pd),
                       (236, 245, pd), (465, 474, pd), (514, 523, pd), (4933, 4942, pd), (320, 328, pd), (532, 555, pd),
                       (712, 715, ps), (830, 853, ps), (903, 911, dv), (927, 936, dv), (1004, 1024, pd), (1293, 1323, of),
                       (1942, 1964, of), (2283, 2292, se), (2816, 2824, dv), (3500, 3508, dv), (2884, 2891, dv),
                       (3513, 3520, dv), (3162, 3165, pt), (3174, 3178, pt), (3310, 3314, pt), (3824, 3827, pt),
                       (3353, 3365, se), (3486, 3496, we), (3738, 3744, pl), (3746, 3756, pl), (3765, 3773, lb),
                       (3829, 3834, ds), (3836, 3839, pf), (3859, 3862, pl), (3863, 3866, pl), (3868, 3872, ol),
                       (3874, 3889, lb), (3891, 3896, lb), (4463, 4498, of), (4516, 4522, of), (4540, 4564, of),
                       (4566, 4579, of), (4581, 4591, of), (4596, 4610, of), (4611, 4618, of), (4623, 4642, of),
                       (4700, 4713, of), (4714, 4749, of), ]}),
    (D6, {"entities": [(94, 117, pd), (129, 140, ql), (142, 153, ql), (155, 165, ql), (170, 180, pd), (454, 478, ps),
                       (501, 517, tm), (1949, 1965, tm), (3744, 3760, tm), (740, 758, ps), (810, 814, pt),
                       (947, 954, dv), (1142, 1149, dv), (1004, 1007, pt), (1073, 1087, se), (1089, 1109, se),
                       (1596, 1602, pl), (3094, 3100, pl), (1736, 1750, se), (1752, 1759, se), (1764, 1774, se),
                       (2412, 2420, of), (2631, 2653, of), (2925, 2942, of), (2947, 2966, of), (2981, 3037, we),
                       (3044, 3087, we), (3138, 3160, cs), (3173, 3192, at), (3215, 3227, at), (3242, 3269, at),
                       (3274, 3291, se), (3310, 3325, ap), (3393, 3398, ap), (3766, 3786, sf), (3809, 3816, ge), ]}),
    (D7, {"entities": [(0, 6, tl), (64, 70, tl), (110, 116, tl), (320, 326, tl), (338, 344, tl), (607, 613, tl),
                       (625, 631, tl), (709, 715, tl), (1023, 1029, tl), (1611, 1617, tl), (2401, 2407, tl),
                       (52, 63, pd), (90, 109, pd), (517, 524, os_), (575, 586, pd), (587, 590, pl), (648, 652, pd),
                       (727, 732, tl), (803, 805, dv), (1894, 1896, dv), (861, 869, dv), (969, 986, ps),
                       (1105, 1115, pd), (1745, 1750, lb), (1784, 1792, ps), ]}),
    (D8, {"entities": [(39, 45, fw), (108, 114, fw), (145, 151, fw), (205, 211, fw), (244, 265, fw), (378, 384, fw),
                       (552, 558, fw), (168, 174, pl), (194, 200, pl), (796, 802, pl), (896, 902, pl), (297, 304, pd),
                       (358, 366, dv), (394, 399, ol), (404, 408, ol), (413, 423, pl), (424, 434, pl), (472, 477, lb),
                       (617, 621, pt), (267, 270, fw), (626, 629, fw), (686, 691, ap), (693, 700, se), (702, 708, dv),
                       (710, 716, pf), (718, 723, os_), (728, 731, tl), (1217, 1229, pf), (1234, 1240, lb),
                       (1542, 1548, pf), (1451, 1458, dv), ]}),
    (D9, {"entities": [(47, 54, pd), (123, 145, ps), (161, 173, dv), (1351, 1363, dv), (1844, 1856, dv),
                       (2938, 2950, dv), (235, 242, tm), (1581, 1588, tm), (517, 533, ai), (2443, 2459, ai),
                       (2723, 2739, ai), (2979, 2995, ai), (399, 402, ps), (421, 424, ps), (915, 918, ps),
                       (1750, 1762, dv), (2189, 2201, dv), (2762, 2774, dv), (2323, 2350, we),
                       (2380, 2386, pl), (2846, 2852, pl), (2405, 2426, ql), (2643, 2665, tm), (2673, 2696, tm),
                       (2891, 2906, se), (2914, 2919, fw), (2921, 2925, lb), (2962, 2974, dv), (3285, 3304, se),
                       (3315, 3330, se), (2091, 2105, ql), ]}),
    (D10, {"entities": [(96, 114, pd), (405, 423, pd), (201, 212, tm), (867, 880, ps), (914, 930, cs),
                        (962, 965, os_), (1050, 1053, os_), (1276, 1279, os_), (1892, 1895, os_), (1925, 1934, se),
                        (1149, 1169, sf), (1827, 1832, pl), (1755, 1806, we), (1352, 1365, ql), (1394, 1406, se),
                        (1939, 1950, se), (1951, 1970, pd), (1990, 2008, ap), (2016, 2036, sf), (2101, 2108, ge),
                        (2189, 2213, se), (2241, 2249, fw), (2254, 2260, tl), (2277, 2288, pd), (2324, 2348, pd),
                        (2365, 2371, fw), (2386, 2393, ap), (2410, 2413, tl), (2418, 2424, pf), (2447, 2459, tm),
                        (2745, 2762, of), (2930, 2960, of), (3179, 3192, of), (3205, 3218, of),
                        (3313, 3333, of), (3349, 3378, of), (3380, 3397, of), (3413, 3427, of), (3517, 3541, of), ]}),
]

if __name__ == '__main__':
    word = "Competitive compensation"

    print_entities(TRAIN_DATA)

    entity_finder(word, D10)
