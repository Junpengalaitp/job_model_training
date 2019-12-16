from constants.category import pl, lb, cs, pt, ds, dv, we, os_, ap, pf
from model_training.training_09.job_desc_09 import *

TRAIN_DATA = [

     (D1, {'entities': [(3670, 3673, os_), (3675, 3682, os_), (5980, 5987, ap), (6174, 6181, ap), (8520, 8527, ap),
                        (8034, 8040, ap), (8127, 8133, ap), (8205, 8211, ap), (8648, 8654, ap), (8661, 8667, ap),
                        (8674, 8680, ap), (1269, 1288, dv), (1600, 1619, dv), (2079, 2098, dv), (8871, 8890, dv),
                        (11345, 11364, dv), (12315, 12358, we), (12359, 12420, we), (12527, 12539, lb), (12521, 12526, lb),
                        (12540, 12547, lb), (12548, 12553, lb), (12554, 12558, lb), (12559, 12565, pl), (12566, 12569, pl),
                        (12153, 12166, lb), (10984, 10988, pf), (10804, 10809, pf), (10876, 10881, pf), (10934, 10939, pf),
                        (11709, 11727, dv)]}),
     (D2, {'entities': [(40, 57, dv), (1032, 1034, dv), (2806, 2808, dv), (6136, 6140, pl), (6142, 6145, pl), (6151, 6161, pl),
                        (6358, 6368, pl), (1328, 1335, lb), (6456, 6463, lb), (1340, 1347, pl), (6465, 6472, pl), (8790, 8797, pl),
                        (1321, 1326, lb), (6474, 6479, lb), (8779, 8784, lb), (6481, 6488, lb), (6494, 6499, lb), (8773, 8777, lb)]}),
     (D3, {'entities': [(476, 485, dv), (6810, 6812, dv), (6929, 6931, dv), (6984, 6989, dv), (7230, 7236, pl), (7237, 7244, ds),
                        (7273, 7286, lb), (7291, 7296, lb)]}),
     (D4, {'entities': [(1310, 1329, dv), (1662, 1681, dv), (2188, 2207, dv), (4539, 4558, dv), (4652, 4671, dv), (5509, 5528, dv),
                        (5923, 5942, dv), (6585, 6604, dv), (7088, 7107, dv), (1444, 1453, dv), (1530, 1539, dv), (1700, 1709, dv),
                        (1928, 1937, dv), (2242, 2251, dv), (2333, 2342, dv), (2516, 2525, dv), (2921, 2930, dv), (3111, 3120, dv),
                        (3191, 3200, dv), (3306, 3315, dv), (2425, 2435, pl), (3433, 3443, pl), (3676, 3686, pl), (3963, 3973, pl),
                        (2451, 2454, os_), (2460, 2467, os_), (2899, 2910, dv), (3368, 3403, we), (3445, 3467, we), (3527, 3529, dv),
                        (3541, 3546, lb), (3892, 3896, pt), (3904, 3911, pl), (3912, 3916, pt), (4226, 4245, pf), (2080, 2085, lb),
                        (3165, 3170, lb), (3479, 3484, lb)]}),
     (D5, {'entities': [(35, 59, dv), (193, 217, dv), (1162, 1172, pl), (1781, 1791, pl), (2642, 2652, pl),
                        (2730, 2740, pl), (1175, 1182, lb), (1184, 1191, lb), (1193, 1198, lb), (1813, 1818, lb),
                        (2745, 2753, lb), (1200, 1206, lb), (1207, 1210, pl), (1793, 1796, pl), (2654, 2657, pl),
                        (1213, 1222, lb), (1798, 1807, lb), (1224, 1231, lb), (1232, 1238, pl), (2659, 2665, pl),
                        (1241, 1247, lb), (3095, 3103, dv), (3107, 3116, dv)]}),
     (D6, {'entities': [(1527, 1533, dv), (3682, 3688, dv), (3700, 3705, os_), (3707, 3713, pl), (3715, 3719, pl), (3758, 3766, ds),
                        (3768, 3777, ds), (3779, 3784, ds), (3786, 3790, ds), (3862, 3869, lb), (3832, 3836, lb), (3838, 3844, lb),
                        (3885, 3890, ap), (3923, 3928, ap), (3929, 3935, ap), (4681, 4684, dv), (5576, 5579, dv)]}),
     (D7, {'entities': [(2191, 2196, os_), (2197, 2201, os_), (2231, 2237, pl), (2239, 2242, pl), (2250, 2260, pl), (2244, 2248, pl),
                        (2262, 2263, pl), (2265, 2270, pl), (2960, 2966, pf), (2967, 2973, pf), (2327, 2343, cs), (142, 158, lb),
                        (348, 364, lb), (1332, 1348, lb), (1842, 1858, lb)]}),
     (D8, {'entities': [(933, 939, pf), (3133, 3139, pf), (3655, 3661, pf), (978, 983, ap), (3142, 3147, ap), (1104, 1123, we),
                        (1157, 1161, pt), (1298, 1302, pt), (1441, 1445, pt), (2138, 2142, pt), (1250, 1256, pl),
                        (1379, 1382, pt), (1558, 1561, pt), (3006, 3009, pt), (1661, 1680, ds), (859, 864, pf), (1899, 1909, ds),
                        (1792, 1795, ds), (2631, 2636, os_), (2657, 2664, os_), (2621, 2625, os_), (4547, 4550, ap), (4926, 4929, dv),
                        (4934, 4937, dv), (5360, 5367, pl), (5379, 5383, pt), (3025, 3028, pf), (5392, 5395, pf)]}),
     (D9, {'entities': [(105, 127, dv), (2888, 2910, dv), (249, 255, pf), (256, 266, pf), (2767, 2777, pf), (271, 281, lb),
                        (352, 358, dv), (1009, 1015, dv), (3010, 3016, dv), (3044, 3050, dv), (4123, 4129, dv),
                        (1016, 1019, dv), (1595, 1614, pf), (2332, 2337, ap), (2384, 2389, ap), (2721, 2729, pf), (4500, 4508, pf),
                        (2731, 2738, lb), (2740, 2749, pf), (4614, 4623, pf), (2751, 2757, pf), (2759, 2765, pf), (4078, 4117, we),
                        (4139, 4179, we), (4180, 4199, we), (4205, 4208, pf), (4222, 4227, os_), (4404, 4413, pf), (4393, 4402, pf),
                        (4385, 4391, pf), (4415, 4422, pf), (4424, 4430, pf), (4555, 4561, pf), (4456, 4478, ap), (4541, 4554, lb)]}),
     (D10, {'entities': [(3168, 3171, ds), (66, 79, dv), (594, 607, dv), (1364, 1377, dv), (3189, 3192, ap), (3269, 3275, pl),
                         (3277, 3281, pl), (3283, 3285, pl), (3316, 3336, ds), (3337, 3352, ds), ]})



]

if __name__ == '__main__':
    ent_dict = {}
    for data in TRAIN_DATA:
        print(data[0])
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            print(entity_name + ": " + entity_type + ' ' + str(entity[0]) + ': ' + str(entity[1]))
            if entity_type not in ent_dict:
                ent_dict[entity_type] = [entity_name]
            else:
                ent_dict[entity_type].append(entity_name)
    for k in ent_dict:
        print(k, set(ent_dict[k]))