from model_training_algo.constants import pl, lf, cs, pt, ds, dv, we, os_, ap, pf, cp
from model_training.training_07.job_desc_07 import *

TRAIN_DATA = [

     (D1, {'entities': [(2654, 2667, lf), (144, 148, pl), (1769, 1773, pl), (2725, 2729, pl), (4153, 4157, pl),
                        (4460, 4464, pl), (1967, 1972, ds), (4471, 4476, ds), (1977, 1985, ds), (4477, 4485, ds),
                        (2053, 2057, pf), (6333, 6337, pf), (2106, 2115, pt), (2194, 2198, pt), (4270, 4274, pt),
                        (3506, 3525, dv), (3527, 3542, dv), (4130, 4135, lf), (4465, 4470, lf), (6011, 6016, lf),
                        (4513, 4523, ap), (5994, 6003, lf), (6270, 6280, pl), (6300, 6305, lf), (6307, 6312, lf),
                        (6317, 6324, lf), (6329, 6332, lf), (6338, 6346, pf), (6347, 6353, pf), (6354, 6357, pl)]}),

     (D2, {'entities': [(1613, 1620, pl), (2916, 2923, pl), (4153, 4160, pl), (4620, 4627, pl), (4673, 4680, pl),
                        (4715, 4722, pl), (3113, 3125, pf), (3762, 3772, pl), (3829, 3839, pl), (3161, 3170, pf),
                        (3137, 3147, pf), (4826, 4836, pf), (4868, 4878, pf), (5226, 5236, pf), (3172, 3180, ds),
                        (4289, 4297, ds), (3774, 3781, pl), (3790, 3800, pl), (2928, 2935, lf), (3859, 3866, lf),
                        (3894, 3899, lf), (1621, 1628, dv), (2274, 2281, dv), (3867, 3874, dv), (2325, 2333, dv),
                        (3900, 3908, dv), (2803, 2807, pt), (2890, 2894, pt), (4101, 4105, pt), (1023, 1026, pt),
                        (4207, 4210, pt), (4468, 4473, os_), (4475, 4479, pt), (3292, 3305, ap)]}),

     (D3, {'entities': [(456, 461, ap), (749, 754, ap), (1006, 1011, ap), (2184, 2189, ap), (2274, 2279, ap), (2484, 2489, ap),
                        (2512, 2517, ap), (2675, 2680, ap), (2860, 2865, ap), (2946, 2951, ap), (3165, 3170, ap), (3499, 3504, ap),
                        (3878, 3883, ap), (3935, 3940, ap), (4158, 4163, ap), (4218, 4223, ap), (4399, 4404, ap), (2048, 2083, we),
                        (349, 354, ap), (2060, 2065, ap), (2895, 2900, ap), (2926, 2931, ap), (4274, 4279, ap),
                        (2130, 2132, ap), (2134, 2138, ap), (3156, 3160, ap), (1935, 1951, cs), (2988, 3001, dv)]}),

     (D4, {'entities': [(63, 67, pt), (324, 328, pt), (556, 560, pt), (589, 593, pt), (785, 789, pt), (858, 862, pt),
                        (2508, 2512, pt), (2581, 2585, pt), (2928, 2932, pt), (3177, 3181, pt), (3324, 3328, pt),
                        (3585, 3589, pt), (3648, 3652, pt), (47, 50, pt), (64, 67, pt), (316, 319, pt), (325, 328, pt),
                        (402, 405, pt), (442, 445, pt), (548, 551, pt), (557, 560, pt), (581, 584, pt), (590, 593, pt),
                        (774, 777, pt), (786, 789, pt), (850, 853, pt), (859, 862, pt), (991, 994, pt), (2501, 2504, pt),
                        (2509, 2512, pt), (2573, 2576, pt), (2582, 2585, pt), (2921, 2924, pt), (2929, 2932, pt),
                        (3169, 3172, pt), (3178, 3181, pt), (3316, 3319, pt), (3325, 3328, pt), (3574, 3577, pt),
                        (3586, 3589, pt), (3641, 3644, pt), (3649, 3652, pt), (630, 634, pl), (820, 824, pl), (2733, 2737, pl),
                        (2783, 2787, pl), (4058, 4062, pl), (4092, 4096, pl), (4103, 4107, pl), (4733, 4737, pl), (4745, 4749, pl),
                        (1328, 1330, pl), (2868, 2870, pl), (5949, 5951, pl), (3016, 3019, pt), (3024, 3027, pt), (3504, 3546, we),
                        (2874, 2880, pl), (4727, 4731, pl), (4733, 4743, pl), (4751, 4754, pl), (4760, 4763, pl), (4772, 4777, lf),
                        (4779, 4784, lf), (4792, 4794, lf), (4796, 4803, lf), (4805, 4811, pf), (4813, 4824, lf), (4826, 4834, pf),
                        (4836, 4841, lf), (4843, 4846, pf), (4848, 4853, ds), (4855, 4860, ds), (4862, 4871, ds), (4873, 4877, lf),
                        (4879, 4883, lf), (5434, 5440, pf)]}),

     (D5, {'entities': [(43, 56, dv), (420, 424, pl), (1662, 1666, pl), (429, 432, pl), (1671, 1674, pl), (1801, 1811, pl),
                        (1901, 1911, pl)]}),

     (D6, {'entities': [(3091, 3153, we), (3999, 4005, dv), (3025, 3030, ap), (3968, 3973, ap), (4054, 4076, ap),
                        (4081, 4101, ap), (473, 476, pf), (4478, 4481, pf), (4873, 4876, pf), (4482, 4487, pf),
                        (4864, 4869, pf), (4493, 4514, we), (3794, 3800, pf), (3802, 3812, pf), (3817, 3827, lf),
                        (5031, 5044, ap), (5011, 5030, cs), (5869, 5891, we)]}),

     (D7, {'entities': [(986, 994, lf), (1008, 1013, pl), (1015, 1021, pl), (1123, 1130, pl), (1161, 1174, lf),
                        (1198, 1208, ds), (1210, 1216, ds), (1225, 1228, pf), (5244, 5248, ap), (4760, 4762, dv),
                        (4732, 4742, dv), (4711, 4719, dv), (4721, 4730, dv), (4744, 4754, dv), (5884, 5887, ds),
                        (3572, 3590, dv), (4106, 4124, dv), (5889, 5907, dv), (5823, 5842, ds)]}),

     (D8, {'entities': [(24, 34, dv), (1060, 1070, pl), (1435, 1445, pl), (2464, 2474, pl), (1073, 1080, lf),
                        (1082, 1089, lf), (1091, 1096, lf), (1467, 1472, lf), (1098, 1104, lf), (1105, 1108, pl),
                        (1447, 1450, pl), (2476, 2479, pl), (1111, 1120, lf), (1452, 1461, lf), (3171, 3180, lf),
                        (1122, 1129, lf), (1130, 1136, pl), (2481, 2487, pl), (1139, 1145, lf), (1183, 1201, dv),
                        (1223, 1229, dv), (1791, 1796, ap), (2422, 2456, we), (2721, 2729, dv), (2733, 2742, dv),
                        (3184, 3190, lf)]}),

     (D9, {'entities': [(25, 35, pl), (289, 292, dv), (2687, 2692, pf), (2284, 2296, ap), (2298, 2314, ap),
                        (2694, 2700, pf), (2766, 2769, pf), (2805, 2808, pf), (2702, 2713, pf), (2718, 2733, pf),
                        (2827, 2834, lf), (2837, 2841, pt), (2842, 2846, pf), (2861, 2868, ds), (2870, 2875, ds),
                        (2877, 2884, ds), (2904, 2910, lf), (2912, 2920, lf), (2974, 2982, lf), (2927, 2936, dv),
                        (2952, 2962, pl), (3072, 3078, pf), (3080, 3087, lf), (3089, 3104, pf)]}),

     (D10, {'entities': [(855, 861, dv), (3922, 3930, dv), (4161, 4169, dv), (2794, 2803, pt), (2843, 2850, pt),
                         (2888, 2892, lf), (2909, 2912, pl), (3126, 3129, pl), (2538, 2547, lf), (2649, 2658, lf),
                         (2757, 2766, lf), (2995, 3004, lf), (3703, 3712, lf), (4343, 4352, lf), (2527, 2537, dv),
                         (3131, 3136, ds), (3138, 3142, pl), (3144, 3154, pl), (3234, 3244, pl), (3155, 3161, lf),
                         (3163, 3166, pl), (3194, 3203, dv), (3220, 3229, lf), (3256, 3261, lf), (3263, 3266, lf),
                         (3329, 3332, ap), (3411, 3415, lf), (3417, 3421, lf)]})

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