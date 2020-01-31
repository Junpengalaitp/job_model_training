from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_data.training_text.job_desc_09 import\
    D1_00095e619f081c90c5a26336e42d135124720499e657585e6df5b9e4a001b109 as D1
    # D2_00a65f8b1c231209dc87a36ebb4368633f9efb4b066f63fbacd887206da380ce as D2, \
    # D3_bb4ce9a8e7a058a95a71fc4fb7eb19fc88682a30ebdbcb82c6d2a1bbfc2aadcc as D3, \
    # D4_02c1fd622a616e2fd1342b5f36ee629892b4d35f44b02b0623055e1c33da55f3 as D4, \
    # D5_9fff53da4939873b545574ffcd62419d6133d44abce0a7b66f2cf4df127a1335 as D5, \
    # D6_d26db8a297034571b0c6bba43468e5bbbe249bdaf2fc5fecf6b023dedbb5b3a0 as D6, \
    # D7_05cc01c480e91e1cff581094b0cb8733aa87fcbe5bb05d83f348b9d7f7824480 as D7, \
    # D8_8ff8d158757cc9b7c53109e58f5be52820be50ccdc86dac04b7933b5c6731f20 as D8, \
    # D9_07b408643d9907a732026749b0557019bb1ab83428d9b1e4fd609f998202f193 as D9, \
    # D10_23635e94f534e182a8dd82030c06c9b5c56280a1829b72cc79c5d176a103cec0 as D10

"""
    Entity order, separated by an empty line
    1. en_core_web_lg entities recognized but unrecognized by custom model
    2. correct entities recognized by custom model
    3. entities not recognized
"""

TRAIN_DATA = [
    (D1, {"entities": [
        (88, 103, 'ORG'), (546, 549, 'CARDINAL'), (4654, 4668, 'TIME'), (4712, 4726, 'TIME'), (4801, 4813, 'ORG'),

        (142, 148, dv), (176, 192, se), (325, 341, tm), (393, 398, ap), (448, 454, dv), (456, 467, se),
        (564, 568, fw), (573, 577, pl), (1159, 1167, dv), (1292, 1298, dv), (1693, 1705, at),
        (1776, 1781, ap), (1862, 1878, tm), (1921, 1927, dv), (1929, 1938, se), (2050, 2069, ps),
        (2482, 2492, ps), (2602, 2616, ap), (2640, 2659, se), (2668, 2680, tm), (2953, 2968, ps),
        (3072, 3080, 'WORK_OF_ART'), (3093, 3109, cs), (3208, 3216, 'WORK_OF_ART'),
        (3227, 3234, 'DATE'), (3238, 3248, we), (3284, 3292, 'WORK_OF_ART'), (3303, 3311, 'DATE'), (3315, 3325, we),
        (3404, 3414, we), (3418, 3434, cs), (3693, 3697, pl), (3698, 3710, pd),
        (3711, 3721, we), (3762, 3763, 'CARDINAL'), (3772, 3773, 'CARDINAL'), (3774, 3784, pl),
        (3791, 3794, tl), (3795, 3802, tl), (3804, 3818, se), (3851, 3853, pl), (3854, 3858, fw), (3859, 3862, ol),
        (3885, 3890, ap), (4180, 4185, ap),
        (4341, 4348, cs),

        (45, 76, pd), (225, 229, se), (1306, 1310, se), (1380, 1384, se), (2071, 2075, se), (473, 484, se),
        (655, 666, sf), (294, 306, se), (1092, 1104, se), (1484, 1496, se), (2189, 2201, se), (2808, 2820, se), (4140, 4152, se),
        (234, 240, se), (1312, 1318, se), (1396, 1402, se), (1827, 1837, ps), (1906, 1919, ap), (2104, 2133, se),
        (280, 293, se), (2206, 2219, se), (3034, 3047, se), (2469, 2475, ap), (2855, 2870, ql), (3111, 3133, cs),
        (3435, 3457, cs), (3666, 3679, fw), (3756, 3761, fw), (3786, 3790, sv), (3839, 3849, tl), (1853, 1855, ap),
        (3920, 3922, ap), (3863, 3873, we), (3891, 3907, tm), (3930, 3951, dv), (3952, 3962, we), (3981, 3991, we),
        (4065, 4075, we), (4002, 4029, cs), (4041, 4056, se), (4087, 4110, ap), (4323, 4331, ds), (4333, 4339, sv),
        (4233, 4245, se),
        ]}),
    # (D2, {"entities": [
    #
    # ]}),
    # (D3, {"entities": [
    #
    # ]}),
    # (D4, {"entities": [
    #
    # ]}),
    # (D5, {"entities": [
    #
    #     ]}),
    # (D6, {"entities": [
    #
    # ]}),
    # (D7, {"entities": [
    # ]}),
    # (D8, {"entities": [
    # ]}),
    # (D9, {"entities": [
    # ]}),
    # (D10, {"entities": [
    #
    # ]})
]

if __name__ == '__main__':
    word = "troubleshoot"

    print_entities(TRAIN_DATA)

    entity_finder(word, D1)
