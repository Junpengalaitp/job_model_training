import unittest
from collections import defaultdict

from model_training_algo.constants import *
from model_training_v2.training_01.train_data_01 import TRAIN_DATA


class TestAnnotations(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.ent_dict = defaultdict(list)
        self.ent_index_list = []
        for data in TRAIN_DATA:
            for entity in data[1]["entities"]:
                entity_type = entity[-1]
                entity_name = data[0][entity[0]: entity[1]]

                self.ent_dict[entity_type].append(entity_name)

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
        print(set(self.ent_dict['PROGRAMMING_LANGUAGE']))
        for word in set(self.ent_dict['PROGRAMMING_LANGUAGE']):
            if word not in pl_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in pl_list)

    def test_OTHER_LANGUAGE(self):
        print(set(self.ent_dict['OTHER_LANGUAGE']))
        for word in set(self.ent_dict['OTHER_LANGUAGE']):
            if word not in ol_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in ol_list)

    def test_LIBRARY(self):
        print(set(self.ent_dict['LIBRARY']))
        for word in set(self.ent_dict['LIBRARY']):
            if word not in lb_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in lb_list)

    def test_FRAMEWORK(self):
        print(set(self.ent_dict['FRAMEWORK']))
        for word in set(self.ent_dict['FRAMEWORK']):
            if word not in fw_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in fw_list)

    def test_ARCHITECT(self):
        if 'CONCEPT' in self.ent_dict:
            print(set(self.ent_dict['ARCHITECT']))
            for word in set(self.ent_dict['ARCHITECT']):
                if word not in at_list:
                    print('the testing word not in list: ', word)
                self.assertTrue(word in at_list)

    def test_PROTOCOL(self):
        print(set(self.ent_dict['PROTOCOL']))
        for word in set(self.ent_dict['PROTOCOL']):
            if word not in pt_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in pt_list)

    def test_DATA_STORAGE(self):
        if 'DATA_STORAGE' in self.ent_dict:
            print(set(self.ent_dict['DATA_STORAGE']))
            for word in set(self.ent_dict['DATA_STORAGE']):
                if word not in ds_list:
                    print('the testing word not in list: ', word)
                self.assertTrue(word in ds_list)

    def test_DIVISION(self):
        print(set(self.ent_dict['DIVISION']))
        for word in set(self.ent_dict['DIVISION']):
            if word not in dv_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in dv_list)

    def test_WORK_EXPERIENCE(self):
        print(set(self.ent_dict['WORK_EXPERIENCE']))
        for word in set(self.ent_dict['WORK_EXPERIENCE']):
            if word not in we_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in we_list)

    def test_OS(self):
        print(set(self.ent_dict['OS']))
        for word in set(self.ent_dict['OS']):
            if word not in os_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in os_list)

    def test_APPROACH(self):
        print(set(self.ent_dict['APPROACH']))
        for word in set(self.ent_dict['APPROACH']):
            if word not in ap_list:
                print('the testing word not in list: ', word)
            self.assertTrue(word in ap_list)

    def test_PLATFORM(self):
        print(set(self.ent_dict['PLATFORM']))
        for word in set(self.ent_dict['PLATFORM']):
            if word not in pf_list:
                print('testing word: ', word)
            self.assertTrue(word in pf_list)

    def test_SOFT_SKILL(self):
        print(set(self.ent_dict['SOFT_SKILL']))
        for word in set(self.ent_dict['SOFT_SKILL']):
            if word not in sf_list:
                print('testing word: ', word)
            self.assertTrue(word in sf_list)

    def test_GENERAL(self):
        print(set(self.ent_dict['GENERAL']))
        for word in set(self.ent_dict['GENERAL']):
            if word not in ge_list:
                print('testing word: ', word)
            self.assertTrue(word in ge_list)

    def test_PRODUCT(self):
        print(set(self.ent_dict['PRODUCT']))
        for word in set(self.ent_dict['PRODUCT']):
            if word not in pd_list:
                print('testing word: ', word)
            self.assertTrue(word in pd_list)

    def test_SERVER(self):
        print(set(self.ent_dict['SERVER']))
        for word in set(self.ent_dict['SERVER']):
            if word not in sv_list:
                print('testing word: ', word)
            self.assertTrue(word in sv_list)

    def test_TOOL(self):
        print(set(self.ent_dict['TOOL']))
        for word in set(self.ent_dict['TOOL']):
            if word not in tl_list:
                print('testing word: ', word)
            self.assertTrue(word in tl_list)


if __name__ == '__main__':
    unittest.main()
