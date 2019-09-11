from database.MongodbManager import MongoManager
from model_training.job_desc import *

pl = "PROGRAMMING_LANGUAGE"
lf = "LIBRARY_OR_FRAMEWORK"
cp = "CONCEPT"
cs = "COMPUTER_SCIENCE"
pt = "PROTOCOL"
ds = "DATA_STORAGE"
dv = "DIVISION"
we = "WORD_EXPERIENCE"
os = 'OS'
ap = 'APPROACH'
pf = 'PLATFORM'

LABELS = [pl, lf, cp, cs, pt, ds, dv, we, os, ap, pf]

pl_list = ['JavaScript', 'HTML', 'CSS', 'PHP', 'ES6', 'Java', 'Kotlin', 'Python', 'Typescript', 'Ruby', 'HTML5']
lf_list = ['React JS', 'React.js', 'React', 'Redux', 'EcmaScript', 'Immutable.js', 'Babel', 'Webpack', 'NPM', 'NGINX',
           'Laravel', 'Flask', 'django', 'scikit-learn', 'Ruby on Rails', 'Node.js', 'jQuery', 'Jenkins', 'Backbone',
           'jUnit', 'Mockito', 'Hamcrest', 'Dagger', 'Terraform', 'Ansible']
cp_list = ['DOM', 'JavaScript object model', 'routing']
cs_list = ['data structure', ]
pt_list = ['RESTful APIs', 'TCP/IP', 'UDP']
ds_list = ['JSON', 'PostgreSQL', 'MongoDB']
dv_list = ['front-end', 'Web Architect', 'architect', 'full stack', 'Android Developer', 'UI designs', 'UI', 'AI',
           'Full Stack Developer', 'QA testers', 'DevOps']
we_list = ['5+ years of experience', '4 years of professional experience', '2-5 years of experience']
os_list = ['Ubuntu', 'Android', 'Debian']
ap_list = ['Agile', 'automated tests', 'Continuous Integration', 'Continuous Delivery', 'CI/CD', 'Scrum', 'XP', 'automated testing',
           ]
pf_list = ['AWS', 'Docker', 'Amazon Web Services', 'Google Cloud Platform', 'GCP', 'Microsoft Azure']

TRAIN_DATA = [
    (D1, {"entities": [(1399, 1407, lf), (1586, 1596, pl), (1608, 1611, cp), (1633, 1656, cp), (1684, 1692, lf),
                       (1783, 1791, lf), (1751, 1756, lf), (1811, 1815, lf), (1819, 1824, lf), (1868, 1878, lf),
                       (1928, 1940, lf), (1896, 1910, cs), (1967, 1972, lf), (2001, 2013, pt), (2069, 2073, ds),
                       (144, 153, dv), (499, 508, dv), (2109, 2118, dv), (2169, 2178, dv), (2205, 2210, lf),
                       (2212, 2219, lf), (2221, 2224, lf)]}),
    (D2, {"entities": [(5, 8, dv), (150, 159, dv), (190, 200, dv), (992, 996, pl), (1001, 1004, pl), (1009, 1019, pl),
                       (1024, 1029, lf), (1034, 1037, pl), (1232, 1235, pl), (1256, 1266, pl), (1268, 1271, pl),
                       (1281, 1288, lf), (1718, 1745, we)]}),
    (D3, {"entities": [(543, 560, dv), (625, 642, dv), (1299, 1316, dv), (1999, 2016, dv), (1529, 1539, dv),
                       (1744, 1746, dv), (2393, 2397, pl), (2424, 2430, pl), (2702, 2707, lf), (2709, 2716, lf),
                       (2722, 2730, lf), (2822, 2828, lf), (2302, 2324, we), ]}),
    (D4, {"entities": [(51, 70, dv), (626, 632, pl), (1238, 1244, pl), (1898, 1904, os), (570, 576, os), (1765, 1771, os),
                       (1905, 1911, os), (933, 935, dv)]}),
    (D5, {"entities": [(998, 1000, dv), (1200, 1202, dv), (1367, 1369, dv), (2517, 2523, pl), (2527, 2533, lf),
                       (2535, 2547, lf), (2549, 2556, lf), (2557, 2567, pl), (2569, 2574, lf), (2575, 2585, ds)]}),
    (D6, {"entities": [(843, 877, we), (375, 379, pl), (805, 809, pl), (814, 827, lf), (719, 724, ap)]}),
    (D7, {"entities": [(980, 990, pl), (1186, 1191, pl), (1331, 1334, pl), (1336, 1343, lf), (1345, 1350, ds),
                       (1352, 1355, pf), (1400, 1403, pf), (1112, 1118, lf), (1364, 1370, pf), (1372, 1379, lf),
                       (1133, 1141, lf), (2441, 2461, dv), (813, 823, dv), (2589, 2599, dv)]}),
    (D8, {"entities": [(1782, 1792, pl), (1794, 1797, pl), (1836, 1843, lf), (1872, 1879, ds)]}),
    (D9, {"entities": [(752, 767, ap), (1606, 1628, ap), (1631, 1650, ap), (1652, 1657, ap), (946, 952, dv),
                       (1397, 1403, dv), (2539, 2561, we), (2705, 2712, lf), (2714, 2721, lf), (2723, 2732, lf),
                       (2941, 2960, pf), (2962, 2965, pf), (2968, 2989, pf), (2991, 2994, pf), (2999, 3014, pf),
                       (3063, 3069, pt), (3071, 3074, pt), (3076, 3083, cp), (3185, 3190, ap), (3192, 3194, ap)]}),
    (D10, {"entities": [(1763, 1780, ap), (1781, 1803, ap), (1663, 1666, pl), (2542, 2565, we)]})]

if __name__ == '__main__':
    for data in TRAIN_DATA:
        for entity in data[1]["entities"]:
            # print(type(entity[0]), entity[1])
            print(data[0][entity[0]: entity[1]] + ": " + entity[-1])
