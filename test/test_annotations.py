import unittest
from collections import defaultdict

from constants.constants import *
from model_training_v2.training_01.train_data_01 import TRAIN_DATA


class TestAnnotations(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.ent_dict = defaultdict(defaultdict)
        self.ent_index_list = []
        for i in range(len(TRAIN_DATA)):
            for entity in TRAIN_DATA[i][1]["entities"]:
                entity_type = entity[-1]
                entity_name = TRAIN_DATA[i][0][entity[0]: entity[1]]
                entity_index = str(i) + ': ' + str(entity[0]) + ', ' + str(entity[1])
                self.ent_dict[entity_type][entity_index] = entity_name

    def test_overlapping_indices(self):
        for data in TRAIN_DATA:
            ent_index_list = []
            for entity in data[1]["entities"]:
                ent_index_list.append((entity[0], entity[1]))
                ent_index_list = sorted(ent_index_list, key=lambda interval: interval[0])
                interval, l = ent_index_list[0], len(ent_index_list)
                for i in range(1, l):
                    interval2 = ent_index_list[i]
                    if interval2[0] < interval[-1]:
                        print(interval2, interval)
                        self.assertTrue(interval2[0] > interval[-1])
                    else:
                        interval = interval2

    def test_PROGRAMMING_LANGUAGE(self):
        if 'PROGRAMMING_LANGUAGE' in self.ent_dict:
            words = set(self.ent_dict['PROGRAMMING_LANGUAGE'].values())
            print(words)
            for index, word in self.ent_dict['PROGRAMMING_LANGUAGE'].items():
                if word not in pl_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in pl_list for word in words]))

    def test_OTHER_LANGUAGE(self):
        if 'OTHER_LANGUAGE' in self.ent_dict:
            words = set(self.ent_dict['OTHER_LANGUAGE'].values())
            print(words)
            for index, word in self.ent_dict['OTHER_LANGUAGE'].items():
                if word not in ol_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ol_list for word in words]))

    def test_LIBRARY(self):
        if 'LIBRARY' in self.ent_dict:
            words = set(self.ent_dict['LIBRARY'].values())
            print(words)
            for index, word in self.ent_dict['LIBRARY'].items():
                if word not in lb_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in lb_list for word in words]))

    def test_FRAMEWORK(self):
        if 'FRAMEWORK' in self.ent_dict:
            words = set(self.ent_dict['FRAMEWORK'].values())
            print(words)
            for index, word in self.ent_dict['FRAMEWORK'].items():
                if word not in fw_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in fw_list for word in words]))

    def test_ARCHITECT(self):
        if 'CONCEPT' in self.ent_dict:
            words = set(self.ent_dict['CONCEPT'].values())
            print(words)
            for index, word in self.ent_dict['CONCEPT'].items():
                if word not in cp_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in cp_list for word in words]))

    def test_PROTOCOL(self):
        if 'PROTOCOL' in self.ent_dict:
            words = set(self.ent_dict['PROTOCOL'].values())
            print(words)
            for index, word in self.ent_dict['PROTOCOL'].items():
                if word not in pt_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in pt_list for word in words]))

    def test_DATA_STORAGE(self):
        if 'DATA_STORAGE' in self.ent_dict:
            words = set(self.ent_dict['DATA_STORAGE'].values())
            print(words)
            for index, word in self.ent_dict['DATA_STORAGE'].items():
                if word not in ds_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ds_list for word in words]))

    def test_DATA_TRANSMISSION(self):
        if 'DATA_TRANSMISSION' in self.ent_dict:
            words = set(self.ent_dict['DATA_TRANSMISSION'].values())
            print(words)
            for index, word in self.ent_dict['DATA_TRANSMISSION'].items():
                if word not in dt_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in dt_list for word in words]))

    def test_COMPUTER_SCIENCE(self):
        if 'COMPUTER_SCIENCE' in self.ent_dict:
            words = set(self.ent_dict['COMPUTER_SCIENCE'].values())
            print(words)
            for index, word in self.ent_dict['COMPUTER_SCIENCE'].items():
                if word not in cs_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in cs_list for word in words]))

    def test_AI(self):
        if 'AI' in self.ent_dict:
            words = set(self.ent_dict['AI'].values())
            print(words)
            for index, word in self.ent_dict['AI'].items():
                if word not in ai_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ai_list for word in words]))

    def test_DIVISION(self):
        if 'DIVISION' in self.ent_dict:
            words = set(self.ent_dict['DIVISION'].values())
            print(words)
            for index, word in self.ent_dict['DIVISION'].items():
                if word not in dv_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in dv_list for word in words]))

    def test_POSITION(self):
        if 'POSITION' in self.ent_dict:
            words = set(self.ent_dict['POSITION'].values())
            print(words)
            for index, word in self.ent_dict['POSITION'].items():
                if word not in ps_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ps_list for word in words]))

    def test_OS(self):
        if 'OS' in self.ent_dict:
            words = set(self.ent_dict['OS'].values())
            print(words)
            for index, word in self.ent_dict['OS'].items():
                if word not in os_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in os_list for word in words]))

    def test_APPROACH(self):
        if 'APPROACH' in self.ent_dict:
            words = set(self.ent_dict['APPROACH'].values())
            print(words)
            for index, word in self.ent_dict['APPROACH'].items():
                if word not in ap_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ap_list for word in words]))

    def test_SOFTWARE_ENGINEERING(self):
        if 'SOFTWARE_ENGINEERING' in self.ent_dict:
            words = set(self.ent_dict['SOFTWARE_ENGINEERING'].values())
            print(words)
            for index, word in self.ent_dict['SOFTWARE_ENGINEERING'].items():
                if word not in se_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in se_list for word in words]))

    def test_PLATFORM(self):
        if 'PLATFORM' in self.ent_dict:
            words = set(self.ent_dict['PLATFORM'].values())
            print(words)
            for index, word in self.ent_dict['PLATFORM'].items():
                if word not in pf_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in pf_list for word in words]))

    def test_SOFT_SKILL(self):
        if 'SOFT_SKILL' in self.ent_dict:
            words = set(self.ent_dict['SOFT_SKILL'].values())
            print(words)
            for index, word in self.ent_dict['SOFT_SKILL'].items():
                if word not in sf_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in sf_list for word in words]))

    def test_GENERAL(self):
        if 'GENERAL' in self.ent_dict:
            words = set(self.ent_dict['GENERAL'].values())
            print(words)
            for index, word in self.ent_dict['GENERAL'].items():
                if word not in ge_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in ge_list for word in words]))

    def test_PRODUCT(self):
        if 'PRODUCT' in self.ent_dict:
            words = set(self.ent_dict['PRODUCT'].values())
            print(words)
            for index, word in self.ent_dict['PRODUCT'].items():
                if word not in pd_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in pd_list for word in words]))

    def test_SERVER(self):
        if 'SERVER' in self.ent_dict:
            words = set(self.ent_dict['SERVER'].values())
            print(words)
            for index, word in self.ent_dict['SERVER'].items():
                if word not in sv_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in sv_list for word in words]))

    def test_TOOL(self):
        if 'TOOL' in self.ent_dict:
            words = set(self.ent_dict['TOOL'].values())
            print(words)
            for index, word in self.ent_dict['TOOL'].items():
                if word not in tl_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in tl_list for word in words]))

    def test_TEAM(self):
        if 'TEAM' in self.ent_dict:
            words = set(self.ent_dict['TEAM'].values())
            print(words)
            for index, word in self.ent_dict['TEAM'].items():
                if word not in tm_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in tm_list for word in words]))

    def test_COMPANY(self):
        if 'COMPANY' in self.ent_dict:
            words = set(self.ent_dict['COMPANY'].values())
            print(words)
            for index, word in self.ent_dict['COMPANY'].items():
                if word not in cp_list:
                    print(f'the testing word not in list: {index, word}')
            self.assertTrue(all([word in cp_list for word in words]))


if __name__ == '__main__':
    unittest.main()
