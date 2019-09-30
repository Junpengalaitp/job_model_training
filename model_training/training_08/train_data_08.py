from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_08.job_desc_08 import *

TRAIN_DATA = [

     (D1, {'entities': [(1071, 1106, we), (1112, 1122, pl), (2484, 2494, pl), (1142, 1149, lf), (2514, 2521, lf),
                        (1154, 1159, lf), (2526, 2531, lf), (1021, 1056, we), (1249, 1254, os), (1256, 1259, ap),
                        (1261, 1264, pf), (1472, 1496, dv), (1408, 1429, dv), (1656, 1664, ap), (1681, 1693, ap),
                        (2323, 2335, ap), (2636, 2648, ap), (4079, 4091, ap), (1382, 1394, ap), (2719, 2731, ap),
                        (2056, 2065, dv), (3843, 3852, dv), (1728, 1733, ap), (2443, 2478, we), (4190, 4238, we),
                        (4254, 4287, we), (1918, 1931, lf), (1911, 1915, pl), (2778, 2791, lf), (2792, 2802, dv),
                        (4353, 4363, dv), (2864, 2873, dv), (4425, 4434, dv), (2875, 2883, dv), (4436, 4444, dv),
                        (2750, 2762, pt), (2629, 2634, ap), (2337, 2359, ap), (2650, 2672, ap), (3723, 3745, ap),
                        (4093, 4115, ap), (2674, 2693, ap), (3747, 3766, ap), (2699, 2705, dv), (3768, 3774, dv)]}),
     (D2, {'entities': [(2422, 2466, we), (137, 146, lf), (449, 458, lf), (1263, 1272, lf), (1889, 1898, lf),
                        (5739, 5748, lf), (5854, 5863, lf), (149, 155, lf), (1804, 1807, dv), (2815, 2832, ap),
                        (2834, 2841, ap), (2887, 2890, pl), (2916, 2921, ap), (3052, 3061, ap), (2972, 2976, os),
                        (3063, 3068, ap), (3070, 3075, ap)]}),
     (D3, {'entities': [(1465, 1471, lf), (1922, 1928, lf), (1406, 1409, pl), (1602, 1612, pl), (1614, 1618, lf),
                        (1620, 1624, ds), (1626, 1629, pl), (1635, 1638, ds), (1640, 1644, pt), (1986, 1989, ap),
                        (1994, 2000, pf), (2037, 2042, ap)]}),
     (D4, {'entities': [(881, 904, dv), (1296, 1299, ds), (3121, 3124, ds), (3892, 3895, ds), (3642, 3658, cs),
                        (3449, 3511, we), (3660, 3671, cs), (3673, 3683, cs), (3909, 3914, ds), (4001, 4006, ds),
                        (4063, 4072, pt), (4777, 4780, pf), (4861, 4864, pf), (4750, 4753, ap), (4101, 4106, ap)]}),
     (D5, {'entities': [(2976, 2983, cp), (2986, 2996, cp), (2028, 2033, ap), (2127, 2132, ap), (3184, 3189, ap),
                        (4340, 4345, ap), (4732, 4737, ap), (3046, 3049, dv), (3138, 3169, we), (1327, 1329, dv),
                        (3308, 3314, pl), (3315, 3320, lf), (3347, 3360, lf), (3461, 3464, pf)]}),
     (D6, {'entities': [(2200, 2206, pl), (3476, 3482, pl), (2208, 2211, pf), (2413, 2416, pf), (2215, 2225, pf),
                        (2418, 2421, pf), (2426, 2431, pf), (2304, 2310, lf), (2312, 2317, lf), (2322, 2327, lf),
                        (2339, 2344, lf), (2345, 2356, lf)]}),
     (D7, {'entities': [(1560, 1573, lf), (3534, 3547, lf), (1654, 1660, pl), (3495, 3501, pl), (1661, 1666, lf),
                        (3502, 3507, lf), (1023, 1026, pt), (1192, 1195, pt), (1386, 1389, pt), (1673, 1676, pt),
                        (3514, 3517, pt), (1921, 1945, dv), (3358, 3389, we), (3266, 3269, dv), (2430, 2435, ap),
                        (2529, 2534, ap), (3428, 3433, ap), (4623, 4628, ap), (4961, 4966, ap)]}),
     (D8, {'entities': [(336, 349, lf), (562, 575, lf), (1236, 1249, lf), (1915, 1928, lf), (2007, 2012, lf),
                        (576, 589, dv), (1250, 1263, dv), (987, 1000, dv), (1496, 1500, pl), (1992, 1996, pl),
                        (1503, 1506, pl), (1999, 2002, pl), (1788, 1824, we), (2013, 2023, pl), (2190, 2193, cp),
                        (2251, 2278, ds), (2280, 2307, cs), (2359, 2364, ap), (2383, 2406, ap), (1321, 1325, pl),
                        (2707, 2742, cs)]}),
     (D9, {'entities': [(807, 832, dv), (1127, 1137, pl), (1140, 1144, pl), (1145, 1148, pl), (1151, 1156, lf),
                        (1168, 1183, dv), (1933, 1990, we), (2788, 2790, pl), (2849, 2851, pl), (2814, 2820, lf),
                        (2842, 2848, lf), (2865, 2873, lf), (2874, 2878, lf), (2879, 2886, lf), (2887, 2892, lf),
                        (2893, 2906, lf), (2907, 2911, lf), (2912, 2922, ds), (2923, 2932, ds), (2933, 2938, ds),
                        (2939, 2952, lf), (2953, 2956, pf), (3168, 3174, pf), (3028, 3030, dv)]}),
     (D10, {'entities': [(242, 259, dv), (261, 263, dv), (3279, 3281, dv), (1748, 1771, dv), (1205, 1210, pf),
                         (1212, 1216, pf), (1218, 1222, ap), (1227, 1237, pf), (2563, 2582, dv), (2512, 2530, dv),
                         (2532, 2550, dv), (2965, 2983, dv), (2880, 2884, pl), (3709, 3714, pl), (2886, 2889, pl),
                         (3716, 3719, pl), (2891, 2893, pl), (5069, 5071, pl), (3098, 3118, dv), (3721, 3725, lf),
                         (3727, 3734, lf), (3741, 3744, lf), (3745, 3750, lf), (3752, 3758, lf),
                         (3759, 3764, lf), (3766, 3772, pl), (3773, 3856, we), (3956, 3959, ap), (3992, 4008, pf)]})



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