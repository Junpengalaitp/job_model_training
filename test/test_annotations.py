import unittest
from model_training.constants import *
from model_training.training_03.train_data_03 import TRAIN_DATA


class TestAnnotations(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.ent_dict = {}
        for data in TRAIN_DATA:
            for entity in data[1]["entities"]:
                entity_type = entity[-1]
                entity_name = data[0][entity[0]: entity[1]]
                if entity_type not in self.ent_dict:
                    self.ent_dict[entity_type] = [entity_name]
                else:
                    self.ent_dict[entity_type].append(entity_name)

    def test_PROGRAMMING_LANGUAGE(self):
        print(set(self.ent_dict['PROGRAMMING_LANGUAGE']))
        for word in set(self.ent_dict['PROGRAMMING_LANGUAGE']):
            if word not in pl_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in pl_list)

    def test_LIBRARY_OR_FRAMEWORK(self):
        print(set(self.ent_dict['LIBRARY_OR_FRAMEWORK']))
        for word in set(self.ent_dict['LIBRARY_OR_FRAMEWORK']):
            if word not in lf_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in lf_list)

    def test_CONCEPT(self):
        if 'CONCEPT' in self.ent_dict:
            print(set(self.ent_dict['CONCEPT']))
            for word in set(self.ent_dict['CONCEPT']):
                if word not in cp_list:
                    print('testing word not in list: ', word)
                self.assertTrue(word in cp_list)

    def test_PROTOCOL(self):
        print(set(self.ent_dict['PROTOCOL']))
        for word in set(self.ent_dict['PROTOCOL']):
            if word not in pt_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in pt_list)

    def test_DATA_STORAGE(self):
        print(set(self.ent_dict['DATA_STORAGE']))
        for word in set(self.ent_dict['DATA_STORAGE']):
            if word not in ds_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in ds_list)

    def test_DIVISION(self):
        print(set(self.ent_dict['DIVISION']))
        for word in set(self.ent_dict['DIVISION']):
            if word not in dv_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in dv_list)

    def test_WORK_EXPERIENCE(self):
        print(set(self.ent_dict['WORK_EXPERIENCE']))
        for word in set(self.ent_dict['WORK_EXPERIENCE']):
            if word not in we_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in we_list)

    def test_OS(self):
        print(set(self.ent_dict['OS']))
        for word in set(self.ent_dict['OS']):
            if word not in os_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in os_list)

    def test_APPROACH(self):
        print(set(self.ent_dict['APPROACH']))
        for word in set(self.ent_dict['APPROACH']):
            if word not in ap_list:
                print('testing word not in list: ', word)
            self.assertTrue(word in ap_list)

    def test_PLATFORM(self):
        print(set(self.ent_dict['PLATFORM']))
        for word in set(self.ent_dict['PLATFORM']):
            if word not in pf_list:
                print('testing word: ', word)
            self.assertTrue(word in pf_list)


if __name__ == '__main__':
    unittest.main()
