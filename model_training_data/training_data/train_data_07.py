from constants.category import pl, ol, lb, fw, cs, pt, ds, dv, we, os_, sv, ap, pf, ps, ge, sf, tl, at, pd, ql, of, tm, \
    se, dt, ai, cp
from model_training_algo.entity_finder import entity_finder, print_entities
from model_training_data.training_text.job_desc_07 import \
    D1_16f7a4c9933a6a40a437ea493c253a621669718cd716a51dacd1257e3059b25b as D1, \
    D2_8387c0335bde4a263f0939c6331fba2fe4a68e48aee796efc6d8a4ab910c532d as D2
    # _cbff4c37f44754e517f4206c7dc83d67ce672e9d19c4e3dbda59e548ba91f3d5 as D3, \
    # _342049c6504576d0f397ff5a5227f10d8b041c3e49184eefbd9d642e5e16a07e as D4, \
    # _42768d7b38b9a784a79f445a17a51957d3284fdaff307b9e75268c1b2776137d as D5, \
    # _b6b0c1c0efdee8ce55c6d972713a08648eb23ed1e93df2295d4e0a364311754a as D6, \
    # _e8e4ba8f369af5ff845013be42a637a74cc8b921e55d37823e94ef930cef5578 as D7, \
    # _d54280607a1242c2cbe628ad5de99cbd4caebb4a626bb3ab2b6b381ff30f9da1 as D8, \
    # _05d843a7745a3e837193f2e1b712551d60e45289aae6f7e1fabec68f223109f5 as D9, \
    # _bda4774869819607aa33a891448c2ac94ca1db76360f6a957e4599ed4df795ad as D10

"""
    Entity order, separated by an empty line
    1. en_core_web_lg entities recognized but unrecognized by custom model
    2. correct entities recognized by custom model
    3. entities not recognized
"""

TRAIN_DATA = [
    (D1, {"entities": [
        (112, 116, 'FAC'), (461, 469, 'DATE'), (473, 482, 'ORG'), (562, 570, 'DATE'),
        (1235, 1252, 'GPE'), (2068, 2085, 'GPE'), (2186, 2197, 'DATE'), (2200, 2211, 'ORG'),

        (35, 38, pl), (521, 528, 'NORP'),
        (679, 682, pl), (884, 892, of), (999, 1029, of),
        (1103, 1108, 'DATE'), (1155, 1159, 'GPE'), (1291, 1298, 'ORG'), (1693, 1710, of),

        (40, 60, cs), (685, 705, cs), (62, 66, os_), (708, 712, os_), (68, 71, cs), (715, 718, cs), (73, 85, cs),
        (721, 733, cs), (25, 33, cs), (148, 156, cs), (668, 676, cs), (1055, 1063, cs), (87, 91, cs), (736, 740, cs),
        (93, 103, sv), (743, 753, sv), (118, 134, cs), (770, 786, cs), (157, 165, ps), (1064, 1072, ps), (326, 328, ai),
        (605, 615, we), (846, 866, of), (810, 833, of), (910, 917, of), (957, 970, of), (972, 975, of),
        ]}),
    (D2, {"entities": [
        (1937, 1954, 'GPE'), (2770, 2787, 'GPE'), (2888, 2899, 'DATE'), (2902, 2913, 'ORG'),

        (25, 32, os_), (58, 61, os_), (70, 81, pl), (87, 90, pf), (92, 101, tl),
        (102, 105, pt), (135, 151, ps), (194, 200, 'GPE'), (238, 245, cp), (366, 389, ai), (484, 487, 'ORG'),
        (669, 692, ai), (710, 715, ap), (782, 798, cs), (849, 858, 'DATE'), (862, 884, we), (897, 916, pd),
        (932, 935, os_), (939, 946, os_), (996, 1012, ai), (1201, 1209, dv),
        (1345, 1361, ai), (1374, 1377, os_), (1379, 1386, os_), (1392, 1395, pf), (1460, 1463, pt),
        (1512, 1519, sv), (1521, 1524, ol), (1525, 1530, ds), (1535, 1538, pf), (1577, 1588, se),
        (1758, 1774, ps), (1805, 1810, 'DATE'),
        (1857, 1861, 'GPE'), (1993, 2000, 'ORG'), (2395, 2412, of),

        (34, 43, cs), (45, 56, cs), (63, 68, pl), (83, 85, ai), (989, 991, ai), (1338, 1340, ai),
        (107, 117, pf), (1466, 1476, pf), (118, 121, pt),  (1477, 1480, pt), (1099, 1124, cp), (1190, 1199, dv),
        (1258, 1268, dv), (1324, 1336, dv), (1396, 1399, tl), (1402, 1428, at), (1657, 1671, dv), (1598, 1609, 'PRODUCT'),
    ]}),
    # (D3, {"entities": [
    #
    # ]}),
    # (D4, {"entities": [
    #
    # ]}),
    # (D5]}),
    # (D6, {"entities": [
    #     ]}),
    # (D7, {"entities": [
    #
    # ]}),
    # (D8, {"entities": [
    # ]}),
    # (D9, {"entities": [
    #
    # ]}),
    # (D10, {"entities": [
    #     (1495, 1513, ge), (475, 481, pd), (1763, 1769, pd), (1770, 1785, se), (1850, 1852, ap), (1853, 1855, ap),
    # ]})
]

if __name__ == '__main__':
    word = "cyber security"

    print_entities(TRAIN_DATA)

    entity_finder(word, D2)
