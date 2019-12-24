from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_03.job_desc_03 import \
    _905bbfecd4553ad91bbcdf9d334dfb1447caaf7afeae10cbec348349e1556936 as D1
    # _696f54ea324f765d42525299d7bca0765be6aca0ec16fa84d01585cfec12bb9c as D2, \
    # _3311541b9f01452f59eaee98039f4a82140e1b41d75da6dfd90f7ffc55051b24 as D3, \
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
    # (D2, {"entities": []}),
    # (D3, {"entities": []}),
    # (D4, {"entities": []}),
    # (D5, {"entities": []}),
    # (D6, {"entities": []}),
    # (D7, {"entities": []}),
    # (D8, {"entities": []}),
    # (D9, {"entities": []}),
    # (D10, {"entities": []}),
]

if __name__ == '__main__':
    word = "awesome customer service"

    print_entities(TRAIN_DATA)

    entity_finder(word, D1)
