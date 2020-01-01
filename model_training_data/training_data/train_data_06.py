from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_data.training_text.job_desc_06 import \
    _e5940376daee8f1fb20214f55d73eab6614d1dc41b6b5e39f0510802281dca7c as D1, \
    _063e170581e747c183b3b59638892084aae5bb57b52ea00d18bf3e63987843d7 as D2
# _c213b25d1182cce917971584991d1aef747d677967eb2dfc490ad45543554d1a as D3, \
# _ae5f6f5c56847e54f10a1a6ba2fa3420744e630f7e6ce76c1f60bf3b4f128ce9 as D4, \
# _9cb6da0cffb3173ef81c4fa03e3beda44459c5c0bf616acf3a043aaa9cba2329 as D5, \
# _30ca4245355909d1dc9f89809c4d7158d6dce8c5f8ff36da555320db3aa80aff as D6, \
# _516a36ab2091b8e70b7c6f638f1830cd0cf49a5e1d4ea93fc6c8b4840d678010 as D7, \
# _1dd6b08b6221b5ebebcf086304b3f2c846eae4a71d833d26d53b250955de811a as D8, \
# _ec4eec423b2b46859324e6f8df6bc44f635d51415a224fc13b36b9eacdf5c223 as D9, \
# _ab44ba20db20d123646df89f89464e37995859d5cbf49b825b86ef32de354dc9 as D10

TRAIN_DATA = [
    (D1, {"entities": [
        # en_core_web_lg entities recognized but unrecognized by custom model
        (0, 7, 'ORG'),
        # correct entities recognized by custom model
        (33, 40, cp), (78, 101, ai),  (672, 674, 'GPE'), (681, 699, ps),
        (873, 883, pl), (913, 920, sv), (922, 925, pt), (939, 946, fw),
        (947, 952, fw), (1001, 1011, pf),
        (1366, 1369, pt), (1400, 1403, pt), (1404, 1416, se), (1450, 1455, lb),
        (1462, 1477, pd), (1631, 1634, pt), (1674, 1684, pl), (1779, 1784, lb),
        (1844, 1865, at), (1938, 1948, pf),
        (2018, 2025, cp), (2171, 2176, 'DATE'), (2191, 2207, ai),
        (2273, 2291, of), (2292, 2310, of), (2322, 2337, of),

        # entities not recognized
        (803, 805, ai), (786, 789, pd), (954, 977, ap), (979, 984, ds), (791, 797, pd), (385, 411, ai),
        (985, 990, lb), (991, 997, pf), (1196, 1203, cp), (1284, 1307, tm), (1489, 1518, ql),
        (1620, 1624, sv), (1646, 1670, ql), (1685, 1695, sf), (1608, 1619, se), (1719, 1730, se),
        (1767, 1778, se), (1337, 1347, se), (1372, 1382, se), (1593, 1603, se), (1731, 1752, ap),
        (1813, 1826, ql), (1904, 1911, sv), (1960, 1969, pf), (2081, 2097, tm), (2209, 2224, ai),
        (2250, 2272, of),
        ]}),
    (D2, {"entities": [
        # en_core_web_lg entities recognized but unrecognized by custom model
        (819, 836, 'GPE'), (2591, 2595, 'CARDINAL'), (2696, 2716, 'TIME'), (2762, 2768, 'TIME'),
        (2804, 2816, 'MONEY'), (2852, 2869, 'GPE'), (3180, 3193, 'TIME'),
        # correct entities recognized by custom model
        (148, 152, 'DATE'), (841, 847, 'GPE'), (1503, 1509, fw), (1568, 1578, fw),
        (1733, 1740, pl), (1784, 1792, at), (1794, 1800, pl), (1834, 1861, pd),
        (1875, 1885, tl), (1996, 2002, pl), (2003, 2009, fw), (2119, 2125, pl), (2140, 2146, fw),
        (2152, 2162, pl), (2874, 2880, 'GPE'),
        # corrected wrong entities recognized by custom model
        (1703, 1717, ql), (1801, 1808, fw), (1961, 1967, pt), (2010, 2013, fw), (2014, 2020, pd),
        # entities not recognized
        (41, 66, ps), (1593, 1613, cs), (1626, 1645, ds), (1545, 1555, se), (1756, 1766, se),
        (1905, 1912, os_), (2282, 2304, of), (2504, 2517, sf), (2578, 2589, of),
    ]}),
    # (D3, {"entities": []}),
    # (D4, {"entities": []}),
    # (D5, {"entities": []}),
    # (D6, {"entities": []}),
    # (D7, {"entities": []}),
    # (D8, {"entities": []}),
    # (D9, {"entities": []}),
    # (D10, {"entities": []})
]

if __name__ == '__main__':
    word = "Contractors"

    print_entities(TRAIN_DATA)

    entity_finder(word, D2)
