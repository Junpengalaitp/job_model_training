from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_05.job_desc_05 import \
    _2905194039672384bcb399eae1fec158b3f872157925ebbb034d97496485f62c as D1
    # _aa17369586948f3637b7dda8a9db905133c9123bccb70bc781a804e8849c0081 as D2, \
    # _bf4a694f7eef157a4208469309d91388cd253e7f93b3c747150e1f696575f99f as D3, \
    # _88d8d77d0462d6fb35c8a965642b727e2a1c9d05e01aaa462d75e21ecdd54b70 as D4, \
    # _7492fc8afd72c14ad860b79a77961c9b6eb9ba3414a70715442959bc013393ff as D5, \
    # _7c7a2be0ff41ee168cd4fdc9a4d8dfb8470d8f504f8bee8a5e5d0fe834898075 as D6, \
    # _8b8db05b3c7bd1801a35d79b6c5a78ba3aab2e0a08c0d5caa2f8e2568672462b as D7, \
    # _23caffb33a533a774389398a3064b1831286a520fbc2471749c9e8a1a62fa2e8 as D8, \
    # _360af1b1ad05eb913aa7d8328e3a4b8d1ae26c2c2453e045725eb1e6c09bdc4e as D9, \
    # _020dd7c157022a1bd8b9722e20cb922cf60dca2489ed28788e0ca63a7bc9ad3c as D10

TRAIN_DATA = [
    (D1, {"entities": [(82, 106, ps), (312, 336, pd), (341, 353, se), (361, 366, pf), (387, 399, tm), (415, 424, ps),
                       (429, 444, ps), (547, 552, ap), (653, 672, pf), (1303, 1322, pf), (3416, 3435, pf), (716, 732, se),
                       (749, 763, pd), (827, 838, se), (843, 853, at), (885, 904, of), (939, 958, pd), (1233, 1240, sv),
                       (1242, 1249, lb), (3231, 3238, lb), (1251, 1260, tl), (3328, 3337, tl), (1262, 1272, ds),
                       (3510, 3520, ds), (1274, 1280, pf), (1282, 1290, tl), (1292, 1298, pf), (1404, 1415, tm),
                       (1848, 1855, ap), (1594, 1613, ge), (1955, 1971, ps), (2144, 2149, fw), (2151, 2159, fw),
                       (2275, 2296, at), (2950, 2966, cs), (3006, 3038, we), (3070, 3074, ol),
                       (3076, 3079, ol), (3084, 3089, ol), (3133, 3142, lb), (3197, 3207, pl), (3222, 3229, sv),
                       (3240, 3245, fw), (3250, 3259, fw), (3278, 3281, pl), (3355, 3361, dv), (3437, 3449, pf),
                       (3451, 3466, pf), (3549, 3566, ap), (3637, 3658, ap), (3694, 3704, lb), (3714, 3718, tl),
                       (3706, 3712, tl), (3754, 3757, pf), (3806, 3809, pf), (3877, 3878, pl), ]}),
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
    word = "R"

    print_entities(TRAIN_DATA)

    entity_finder(word, D1)
