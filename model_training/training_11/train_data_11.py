from model_training.constants import pl, lf, cs, pt, ds, dv, we, os, ap, pf, cp
from model_training.training_11.job_desc_11 import *

TRAIN_DATA = [

    (D1, {'entities': [(170, 183, dv), (2814, 2827, dv), (287, 290, pl), (2493, 2496, pl), (2738, 2741, pl),
                       (3050, 3053, pl), (3919, 3922, pl), (388, 397, lf), (1031, 1040, lf), (1098, 1107, lf),
                       (1222, 1231, lf), (1926, 1935, lf), (2755, 2764, lf), (332, 352, dv), (1865, 1885, dv),
                       (2472, 2476, ap), (3714, 3718, ap), (2516, 2531, ap), (2743, 2753, pl), (3981, 3991, pl),
                       (2925, 2928, ap), (2993, 3001, pt), (3004, 3008, pt), (3992, 4000, dv), (3879, 3882, pt),
                       (4065, 4088, ds), (4041, 4060, ds), (2678, 2703, we)]}),
    (D2, {'entities': [(36, 51, dv), (85, 91, dv), (2072, 2078, dv), (2115, 2121, dv), (2478, 2484, dv), (2694, 2700, dv),
                       (2871, 2877, dv), (3351, 3357, dv), (122, 125, os), (2919, 2922, os), (3737, 3740, os),
                       (130, 137, os), (2953, 2960, os), (3745, 3752, os), (2332, 2337, lf), (2887, 2892, lf), (3813, 3818, lf),
                       (2436, 2438, dv), (2701, 2703, dv), (2895, 2905, pl), (3823, 3833, pl), (2976, 2982, pl), (3104, 3117, lf),
                       (3125, 3137, pl), (3142, 3146, pl), (3149, 3153, pl), (3199, 3203, pt), (3204, 3207, pf), (3215, 3221, pf), ]}),
    (D3, {'entities': [(973, 977, pl), (2159, 2163, pl), (2265, 2269, pl), (979, 984, lf), (2208, 2213, lf), (266, 285, ap),
                       (567, 592, dv), (684, 709, dv), (1042, 1052, ds), (1063, 1069, pl), (1080, 1085, lf), (1098, 1106, dv),
                       (1113, 1128, ap), (1286, 1292, pf), ]}),
    (D4, {'entities': [(11, 25, dv), (941, 966, dv), (495, 499, pf), (1297, 1301, pf), (1322, 1334, dv), (1870, 1884, os),
                       (2425, 2431, pt), (2433, 2437, pt), (2528, 2537, pf), (2539, 2546, pf), (2548, 2555, pf), (2557, 2573, pf),
                       (2594, 2606, pf), (1835, 1842, os), (2607, 2614, os), (1825, 1830, os), (2673, 2689, cs), (3700, 3708, dv)]}),
    (D5, {'entities': [(0, 17, dv), (247, 264, dv), (2323, 2340, dv), (1063, 1070, lf), (59, 76, dv), (518, 526, dv),
                       (681, 689, dv), (729, 737, dv), (825, 833, dv), (1038, 1046, dv), (1584, 1592, dv), (546, 556, pl), (1006, 1016, pl),
                       (2396, 2406, pl), (2530, 2541, lf), (568, 573, lf), (837, 841, ds), (786, 791, pf), (793, 799, pf), (803, 811, pf),
                       (842, 851, pt), (1077, 1086, pt), (1609, 1618, pt), (1091, 1098, pl), (1620, 1627, pl), (2148, 2153, ap),
                       (2158, 2163, ap), (2437, 2440, pl), (2359, 2379, we), (2442, 2512, we), (2588, 2592, lf), (2594, 2598, lf),
                       (2606, 2609, pl), (2756, 2759, pl), (2677, 2681, lf), (2682, 2685, lf), (2686, 2690, lf), (2750, 2754, pl),
                       (2781, 2785, lf), (2910, 2926, cs), (3180, 3199, cs), (3074, 3089, cs),
                       ]}),
    (D6, {'entities': [(2400, 2404, pl), (283, 286, pl), (1197, 1200, pl), (1537, 1540, pl), (2235, 2238, pl), (2287, 2290, pl),
                       (2326, 2329, pl), (1202, 1207, ds), (2630, 2635, ds), (1209, 1213, lf), (1508, 1511, pl), (2049, 2052, pl),
                       (1541, 1551, ap), (2715, 2725, ap), (1950, 1959, dv), (2202, 2211, dv), (3525, 3534, dv), (3902, 3911, dv),
                       (2454, 2464, pl), (2481, 2490, lf), (2243, 2248, lf), (3003, 3008, lf), (2561, 2570, pt), (2596, 2604, pt),
                       (3010, 3013, lf), (3015, 3019, lf), (3042, 3048, lf), (3173, 3178, os), (3360, 3366, pf), (3370, 3377, pf),
                       (3546, 3550, lf), (3552, 3555, lf), (3557, 3562, pf), (3564, 3569, pf), (3859, 3864, ds), (3866, 3875, ds),
                       (3881, 3888, ds), (3384, 3387, ap), (4012, 4024, ap),
                       ]}),
    (D7, {'entities': [(1262, 1279, dv), (1364, 1374, pl), (1683, 1693, pl), (3111, 3121, pl), (1376, 1384, lf), (1390, 1391, pl),
                       (1442, 1443, pl), (1392, 1395, pl), (1435, 1440, pl), (1448, 1450, pl), (1327, 1329, pl), (1662, 1664, pl),
                       (3070, 3072, pl), (1997, 1999, dv), (3043, 3064, we), (2938, 2973, we), (3086, 3105, we), ]}),
    (D8, {'entities': [(1685, 1695, cs), (2397, 2407, cs), (3679, 3689, cs), (3789, 3799, cs), (1580, 1597, dv), (2818, 2820, pl),
                       (2824, 2827, pl), (3544, 3547, pl), (3572, 3575, pl), (3285, 3301, cs), (3303, 3314, cs), (3367, 3372, ap),
                       (3374, 3379, ap), (3381, 3387, ap), (2755, 2778, we), (2998, 3010, ap), ]}),
    (D9, {'entities': [(58, 73, dv), (226, 241, dv), (773, 776, pf), (941, 944, pf), (2833, 2836, pf), (3089, 3092, pf),
                       (3410, 3413, pf), (3756, 3759, pf), (4315, 4318, pf), (813, 816, pf), (818, 829, pf), (835, 838, pf),
                       (863, 866, pf), (1348, 1366, dv), (902, 911, pf), (1380, 1389, pf), (1256, 1262, pf), (2534, 2539, ap),
                       (2737, 2742, os), (2761, 2806, we), (2812, 2831, pf), (4079, 4098, pf),
                       (2838, 2852, we), (2853, 2856, ds), (2868, 2873, ds), (2875, 2881, ds), (2883, 2891, ds), (2921, 2925, pl),
                       (2926, 2932, pl), (2974, 2981, lf), (890, 897, lf), (2983, 2990, lf), (3039, 3046, lf), (3027, 3033, lf),
                       (2996, 3019, ap), (3034, 3038, lf), (3093, 3096, pf), (3098, 3108, pf), (3374, 3384, pf), (3422, 3432, pf),
                       (3110, 3118, pf), (3119, 3124, pf), (3458, 3466, lf), (3468, 3475, ds), (3487, 3492, pf), (3510, 3516, ds),
                       (3527, 3532, lf), (4291, 4296, lf), (3684, 3687, pt), (3703, 3706, pt), (3713, 3720, cp),
                       (2632, 2635, pt), (3708, 3711, pt), (2667, 2670, pt), (3722, 3725, pt), (3760, 3763, pf), (3791, 3793, pf),
                       (4319, 4321, pf), (3819, 3823, lf), (3965, 3969, ds), (3972, 3975, pl), (4025, 4029, pt), (4110, 4120, ds),
                       (4122, 4130, ds), (4138, 4143, ds), (4145, 4152, ds), (4164, 4170, pl), (4173, 4178, pl), (4181, 4186, pl),
                       (4189, 4195, pl), (4198, 4208, pl), (4211, 4215, pl), (4218, 4222, pl), (4342, 4348, pf), (3591, 3599, lf),
                       (4243, 4251, lf), ]}),
    (D10, {'entities': [(140, 142, dv), (476, 478, dv), (697, 699, dv), (1027, 1029, dv), (3065, 3067, dv), (228, 238, dv),
                        (365, 375, dv), (549, 559, dv), (1946, 1956, dv), (2067, 2077, dv), (2283, 2300, dv), (2335, 2338, pt),
                        (3166, 3204, we), (3443, 3448, os), (3450, 3456, pl), (1848, 1854, pf), (3458, 3464, pf),
                        (3511, 3514, dv), (3466, 3476, pf), ]})

]

