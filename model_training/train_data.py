from database.MongodbManager import MongoManager
from model_training.job_desc import *

pl = "PROGRAMMING_LANGUAGE"
lf = "LIBRARY_OR_FRAMEWORK"
cp = "CONCEPT"
cs = "COMPUTER_SCIENCE"
pt = "PROTOCOL"
ds = "DATA_STORAGE"
dv = "DIVISION"

pl_list = ['JavaScript', ]
lf_list = ['React JS', 'React.js', 'React', 'Redux', 'EcmaScript', 'Immutable.js', 'Babel', 'Webpack', 'NPM']
cp_list = ['DOM', 'JavaScript object model']
cs_list = ['data structure',]
pt_list = ['RESTful APIs']
ds_list = ['JSON']
dv_list = ['front-end']

TRAIN_DATA = [(D1, {"entities": [(1399, 1407, lf), (1586, 1596, pl), (1608, 1611, cp), (1633, 1656, cp), (1684, 1692, lf),
                                 (1783, 1791, lf), (1751, 1756, lf), (1811, 1815, lf), (1819, 1824, lf), (1868, 1878, lf),
                                 (1928, 1940, lf), (1896, 1910, cs), (1967, 1972, lf), (2001, 2013, pt), (2069, 2073, ds),
                                 (144, 153, dv), (499, 508, dv), (2109, 2118, dv), (2169, 2178, dv), (2205, 2210, lf),
                                 (2212, 2219, lf), (2221, 2224, lf)]})]
