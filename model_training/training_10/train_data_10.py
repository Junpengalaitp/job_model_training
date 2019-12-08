from model_training_algo.constants import pl, lb, cs, pt, ds, dv, we, os_, ap, pf, cp
from model_training.training_10.job_desc_10 import *

TRAIN_DATA = [

    (D1, {'entities': [(106, 118, dv), (1427, 1439, dv), (3161, 3164, ds), (2549, 2563, ds), (3270, 3284, ds),
                       (3332, 3338, pl),
                       (3343, 3349, lb)]}),
    (D2, {'entities': [(2416, 2438, ap), (790, 819, dv), (2446, 2448, dv), (3667, 3677, pl), (3712, 3722, pl),
                       (4759, 4769, pl),
                       (3515, 3519, pl), (3638, 3642, pl), (4570, 4574, pl), (3535, 3538, ds), (3733, 3739, lb),
                       (4591, 4598, lb),
                       (3629, 3633, pl), (3634, 3637, pl), (3797, 3802, lb), (3807, 3814, lb), (4507, 4514, pt),
                       (4515, 4519, ds),
                       (4520, 4523, pt), (4646, 4651, ds), (4658, 4665, lb), (4674, 4679, ds), (4580, 4585, lb),
                       (4770, 4773, cp),
                       (1543, 1545, dv), (3619, 3621, dv), (4741, 4743, dv), (5001, 5004, pf), (5025, 5031, pf),
                       (5033, 5040, lb),
                       (5042, 5048, lb), (5050, 5055, lb), (5057, 5061, lb), (5063, 5068, lb), (5070, 5076, pf), ]}),
    (D3,
     {'entities': [(105, 107, dv), (206, 208, dv), (110, 116, dv), (237, 243, dv), (1072, 1078, dv), (3803, 3809, dv),
                   (2734, 2741, pf), (4682, 4689, pf), (2743, 2749, pl), (2751, 2754, pl), (2756, 2766, pf),
                   (2771, 2774, pf),
                   (4002, 4005, pf), (3035, 3047, dv), (3939, 3942, ap), (3944, 3947, ap), (3949, 3954, ap),
                   (3956, 3959, ap),
                   (3964, 3968, ap), (4065, 4078, lb), (4021, 4024, pf), (4026, 4029, pf), (4031, 4033, pf),
                   (4035, 4038, pf),
                   (4040, 4050, pf), (4110, 4115, os_), (4209, 4214, ds), (4216, 4226, ds), (4571, 4587, lb),
                   (514, 517, dv),
                   (2337, 2340, dv), (4975, 4978, dv), ]}),
    (D4,
     {'entities': [(20, 22, pl), (2986, 2988, pl), (3032, 3034, pl), (3509, 3511, pl), (4009, 4011, pl), (237, 244, dv),
                   (249, 268, dv), (270, 282, dv), (287, 296, dv), (3704, 3720, cs), (3475, 3482, dv), (3630, 3642, ap),
                   (554, 566, ap), (3644, 3656, ap), (3002, 3021, we), (939, 942, pt), (2620, 2623, pt),
                   (3826, 3835, pt),
                   (3765, 3770, ds), (3775, 3782, ds), (4013, 4019, pf), (4021, 4031, pf), ]}),
    (D5, {'entities': [(144, 148, dv), (3268, 3272, dv), (604, 623, dv), (1514, 1526, pf), (2823, 2844, pf),
                       (3865, 3886, pf),
                       (1586, 1598, pf), (3999, 4011, pf), (2784, 2787, pf), (2927, 2930, pf), (2934, 2939, pf),
                       (2756, 2761, os_),
                       (3014, 3019, os_), (2742, 2745, ds), (3196, 3199, ds), (3771, 3774, ds), (2763, 2767, lb),
                       (3726, 3733, lb),
                       (3735, 3741, lb), (3743, 3746, cp), (3748, 3756, lb), (3758, 3760, pl), (3208, 3215, os_),
                       (3787, 3794, os_),
                       (3088, 3095, pf), (3828, 3835, pf), (3078, 3086, pf), (3818, 3826, pf), (3104, 3108, pf),
                       (3994, 3998, ap),
                       (3971, 3980, pf), (3887, 3897, pf), ]}),
    (D6, {'entities': [(1618, 1628, pl), (377, 387, dv), (940, 950, dv), (3980, 3990, dv), (1691, 1695, ds),
                       (1807, 1811, ds),
                       (3301, 3304, os_), (3338, 3341, os_), (3435, 3438, os_), (3284, 3290, dv)
                       ]}),
    (D7, {'entities': [(144, 154, dv), (537, 547, dv), (944, 954, dv), (684, 688, pl),
                       (2534, 2538, pl), (4019, 4023, pl), (690, 695, lb), (2540, 2545, lb), (4025, 4030, lb),
                       (701, 706, lb), (2551, 2556, lb), (4036, 4041, lb), (746, 756, dv),
                       (1780, 1790, dv), (2045, 2055, dv), (656, 665, dv), (3474, 3483, dv), (3601, 3610, dv),
                       (3985, 3994, dv), ]}),
    (D8, {'entities': [(1623, 1648, dv), (3512, 3538, we), (3594, 3599, ap), (3738, 3747, dv), (2047, 2067, dv), (3769, 3779, pl),
                       (3781, 3785, pl), (3787, 3790, pl), (3795, 3800, lb), (3921, 3941, ds), (4044, 4047, pf), (4048, 4070, ap),
                       (3954, 3964, ds), (3965, 3971, pf), (4072, 4078, pf), (4094, 4111, ap), (4123, 4125, ap), (4205, 4210, lb),
                       (4212, 4220, lb), (3817, 3841, ap), (4226, 4234, lb), (4235, 4242, lb), ]}),
    (D9, {'entities': [(26, 28, dv), (205, 207, dv), (3030, 3032, dv), (3215, 3217, dv), (308, 315, os_), (320, 323, os_),
                       (2179, 2204, dv), (2578, 2585, pf), (2587, 2593, pl), (3550, 3556, pl), (2595, 2598, pl), (2600, 2610, pf),
                       (4370, 4380, pf), (2615, 2618, pf), (4147, 4150, pf), (2651, 2667, lb), (2782, 2798, lb), (3091, 3107, lb),
                       (3333, 3349, lb), (3269, 3299, we), (3404, 3431, dv), (3433, 3436, dv), (3594, 3597, dv), (3498, 3522, cs),
                       (3524, 3527, cs), (3533, 3541, cs), (3581, 3588, lb), (3809, 3816, lb), (3617, 3622, lb), (3627, 3632, lb),
                       (3655, 3670, dv), (3706, 3734, cs), (3736, 3739, cs), (3821, 3826, lb), (4084, 4087, ap), (4089, 4092, ap),
                       (4094, 4099, ap), (4101, 4104, ap), (4109, 4113, ap), (3788, 3805, cs), (4166, 4169, pf), (4171, 4174, pf),
                       (4176, 4178, pf), (4180, 4183, pf), (4185, 4195, pf), (4197, 4208, pf), (4210, 4223, lb), (4252, 4258, dv),
                       (4483, 4488, ds), (4490, 4500, ds), ]}),
    (D10, {'entities': [(33, 38, pf), (352, 357, pf), (731, 736, pf), (984, 989, pf), (1451, 1456, pf), (791, 801, dv), (1980, 1990, dv),
                        (803, 812, dv), (1995, 2004, dv), (818, 828, dv), (1942, 1956, dv), (1672, 1675, dv), (2484, 2486, dv),
                        (3457, 3459, dv), (3515, 3517, dv), (2281, 2300, dv), (4356, 4375, dv), (4548, 4567, dv), (4320, 4338, we),
                        (4416, 4436, dv), (4069, 4086, ap), (4195, 4203, dv), (4182, 4193, dv), (4801, 4812, dv), (4465, 4487, ap),
                        (4441, 4463, cp), (4855, 4869, pf)]})

]

