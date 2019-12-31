from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import print_entities, entity_finder
from model_training_v2.training_05.job_desc_05 import \
    _2905194039672384bcb399eae1fec158b3f872157925ebbb034d97496485f62c as D1, \
    _0a3cd5d4ed4260e481675ed402143437c02d2dc4d2b4833ed73bfc3dc13f46ed as D2, \
    _ccee86da9ac7d690f481f1608674340e493746fc778b7527071524e67e834758 as D3, \
    _536b29e61ffc30da72f593a75d2b525d8692b3275d2082c3505cd17a0c851691 as D4, \
    _b6d663e20f5bbb87b093e6fc205c84698ac4df0b27e9bee67413d5d9dd69f836 as D5, \
    _59044555d5f71bf896f101f5e473abd6e94d4ec1c6add3067525161d02558baa as D6, \
    _f0d983532275eb28b48dbd231a248ed11782d481cb8c553c2073de10f9c41754 as D7, \
    _9286830d27cce6fa260d73a979a881c778319b5dec2a50ea6b313fd2aff45671 as D8, \
    _28238ff7edf1d1ee3988476dd7bec883fb973a20f62e9ea4e9f21c3312c3fb74 as D9, \
    _d9d8fff2d80957b12a4d1911a003d56f0df647e415ef1c31fa3e869a692ef056 as D10

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
    (D2, {"entities": [(71, 87, ps), (133, 144, of), (172, 178, fw), (179, 185, fw), (188, 198, pl), (199, 202, pl),
                       (246, 263, ps), (421, 445, ps), (305, 316, of), (344, 346, pl), (353, 355, pl),
                       (360, 373, at), (564, 577, at), (374, 377, ol), (447, 450, pt), (494, 506, of),
                       (534, 537, pt), (538, 543, pf), (544, 563, pf), (578, 593, pf), ]}),
    (D3, {"entities": [(65, 80, ps), (117, 124, tl), (125, 132, tl), (133, 152, pf), (153, 159, pl), (285, 291, pl),
                       (160, 165, ol), (265, 268, pl), (269, 276, sv), (277, 284, fw), (292, 297, fw), ]}),
    (D4, {"entities": [(65, 97, ps), (147, 157, ol), (331, 341, ol), (158, 170, pd), (312, 319, se),
                       (342, 357, ap), (320, 330, ds), (358, 368, dv), ]}),
    (D5, {"entities": [(65, 91, ps), (94, 119, ps), (157, 169, of), (387, 399, of), (172, 178, of),
                       (402, 408, of), (186, 188, pl), (350, 352, pl), (440, 442, pl), (189, 192, pt), (193, 203, pl),
                       (463, 473, pl), (204, 223, pf), (443, 462, pf), (279, 304, ps), (334, 346, pd), (416, 439, pd),
                       (474, 478, fw), ]}),
    (D6, {"entities": [(83, 87, fw), (151, 162, of), (179, 189, pl), (452, 462, pl), (190, 201, fw),
                       (205, 219, lb), (268, 293, ps), (202, 204, pl), (339, 341, pl), (429, 431, pl), (376, 388, of),
                       (165, 171, of), (391, 397, of), (405, 428, pd), (432, 451, pf), (463, 467, fw), ]}),
    (D7, {"entities": [(76, 100, ps), (264, 288, ps), (168, 174, pl), (360, 366, pl), (175, 181, fw), (367, 373, fw),
                       (182, 194, pd), (195, 214, pf), (344, 359, of), (374, 385, lb), ]}),
    (D8, {"entities": [(74, 94, ps), (146, 157, of), (165, 183, at), (184, 203, pf), (204, 225, pf), (226, 235, tl),
                       (236, 246, pf), (247, 255, ps), ]}),
    (D9, {"entities": [(78, 88, pl), (89, 99, pl), (100, 104, sv), (192, 204, of), (212, 222, pl), (223, 230, sv),
                       (231, 241, pl), (242, 249, ds), (250, 269, pf), ]}),
    (D10, {"entities": [(220, 225, tl), (236, 243, os_), (244, 247, os_), (320, 333, tl), (338, 341, tl),
                        (412, 430, tl), (431, 449, tl), (450, 463, tl), (464, 467, tl), (468, 474, pf),
                        (558, 574, ai), (638, 654, ai), (655, 670, ai), (671, 673, pl), (674, 680, pl),
                        (836, 857, pf), (748, 771, dv), (858, 863, pf), (864, 883, pf), (884, 898, dv), ]}),
]

if __name__ == '__main__':
    word = "cloud-security"

    print_entities(TRAIN_DATA)

    entity_finder(word, D10)