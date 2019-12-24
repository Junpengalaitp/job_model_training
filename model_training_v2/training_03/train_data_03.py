from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_03.job_desc_03 import \
    _905bbfecd4553ad91bbcdf9d334dfb1447caaf7afeae10cbec348349e1556936 as D1, \
    _3920e62585070842db9dff466177940ee369dd923a5ae5df3867328cbc84c9ca as D2, \
    _cc8087173d6b932401c18b84640cc5e14a6fd58dabe138851328a71b1cd285dc as D3
    # _309ce74603f4d3a7e222fa9785a6f5e0d1670d1c3dda1dbb3826d6148437b734 as D4, \
    # _e0eb1c1637e0227bca225beea9405cd47f16fd161c393a64754e1b60d3c7bf59 as D5, \
    # _fba8599e36e5fb7181f122265858b92d708a32233ca6c47177254a3fe6e4a431 as D6, \
    # _a27147c87413de7fd486418b9f291ea93a5234b68e6c9a68a841b049678501c1 as D7, \
    # _bb05ff489a277988a5c505d8bd105a13adec52e5bbe58e52d52d573f842d567a as D8, \
    # _e69b49c4cb81ffe3749f3102d8cab6de3f1fb9dee0b30c98a4b5c39c2dd05994 as D9, \
    # _ef4185606d7cb286d3e256864d93bcd6470e5a6059cc630a54f1b93bd3ba2d33 as D10

TRAIN_DATA = [
    (D1, {"entities": [(27, 42, pd), (70, 92, cp),  (724, 740, cp), (910, 929, pd), (1296, 1315, pd), (942, 958, ql),
                       (969, 977, dv), (1317, 1328, pl), (1723, 1734, pl), (1330, 1337, os_), (1742, 1749, os_),
                       (1404, 1420, ai), (1474, 1483, ap), (1501, 1507, pd), (1510, 1517, dv), (1648, 1664, cs),
                       (1736, 1739, os_), (1751, 1757, pl), (1759, 1762, ol), (1764, 1780, ai), (2651, 2658, pd),
                       (2771, 2781, pd), (2928, 2952, pd), ]}),
    (D2, {"entities": [(17, 31, ps), (93, 105, ql), (256, 269, tm), (384, 387, os_), (442, 447, pl), (452, 463, pl),
                       (486, 495, ps), (534, 559, sf), (569, 587, cp), (637, 653, cs), (672, 703, we), (839, 850, of),
                       (982, 992, of), (1006, 1012, of), (1044, 1050, of), (1150, 1157, of)]}),
    (D3, {"entities": [(46, 59, ps), (124, 144, ge), (210, 235, ge), (237, 265, sf), (267, 282, ge), (2083, 2098, ge),
                       (606, 621, ps), (828, 830, dv), (860, 872, ql), (1873, 1910, we), (835, 849, ps),
                       (1912, 1950, we), (1954, 1959, pl), (2376, 2381, pl), (1962, 1965, os_),
                       (2034, 2043, at), (2048, 2052, dt), (2140, 2151, cs), (2158, 2164, pf), (2179, 2186, ge),
                       (2221, 2229, ds), (2231, 2242, tl), (2262, 2272, pt), (2274, 2278, tl), (2274, 2278, tl),
                       (2289, 2294, ap), (2296, 2304, tl), (2306, 2311, tl), (2473, 2478, tl), (2313, 2319, tl),
                       (2321, 2327, pf), (2336, 2346, tl), (2382, 2397, se), (2399, 2402, at), (2416, 2420, at),
                       (2443, 2463, of), (2306, 2311, tl), (2473, 2478, tl), (2868, 2877, of), (2780, 2799, of),
                       (2921, 2938, of), (3005, 3011, of), (4277, 4293, tm), ]}),
    # (D4, {"entities": []}),
    # (D5, {"entities": []}),
    # (D6, {"entities": []}),
    # (D7, {"entities": []}),
    # (D8, {"entities": []}),
    # (D9, {"entities": []}),
    # (D10, {"entities": []}),
]

if __name__ == '__main__':
    word = "code reviewers"

    print_entities(TRAIN_DATA)

    entity_finder(word, D3)
