import re

from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_02.job_desc_02 import \
    _45f21e8cc59d13ba57e5ad2f0366fac7093672f223b8e7c119b45e16d4dc0f6c as D1, \
    _696f54ea324f765d42525299d7bca0765be6aca0ec16fa84d01585cfec12bb9c as D2, \
    _3311541b9f01452f59eaee98039f4a82140e1b41d75da6dfd90f7ffc55051b24 as D3, \
    _309ce74603f4d3a7e222fa9785a6f5e0d1670d1c3dda1dbb3826d6148437b734 as D4
    # _9cb6da0cffb3173ef81c4fa03e3beda44459c5c0bf616acf3a043aaa9cba2329 as D5, \
    # _30ca4245355909d1dc9f89809c4d7158d6dce8c5f8ff36da555320db3aa80aff as D6, \
    # _516a36ab2091b8e70b7c6f638f1830cd0cf49a5e1d4ea93fc6c8b4840d678010 as D7, \
    # _1dd6b08b6221b5ebebcf086304b3f2c846eae4a71d833d26d53b250955de811a as D8, \
    # _ec4eec423b2b46859324e6f8df6bc44f635d51415a224fc13b36b9eacdf5c223 as D9, \
    # _ab44ba20db20d123646df89f89464e37995859d5cbf49b825b86ef32de354dc9 as D10

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
                       (1845, 1862, ap), (1913, 1927, se), (1942, 1950, tl), (1955, 1959, tl), (2025, 2041, cs), ]})
]

if __name__ == '__main__':
    word = "computer science"

    print_entities(TRAIN_DATA)

    entity_finder(word, D4)
