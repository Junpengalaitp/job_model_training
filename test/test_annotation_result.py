import unittest
from collections import defaultdict

from constants.constants import *
from model_training_data.training_data.train_data_08 import TRAIN_DATA


class TestAnnotations(unittest.TestCase):

    def setUp(self) -> None:
        """change TRAIN_DATA to a dict[dict]
           outer key: category
           inner key : article number + ":" + entity start index + "," + entity end index
           inner value: entity word
        """
        super().setUp()
        self.ent_dict = defaultdict(defaultdict)
        for i in range(len(TRAIN_DATA)):
            for entity in TRAIN_DATA[i][1]["entities"]:
                entity_category = entity[-1]
                entity_name = TRAIN_DATA[i][0][entity[0]: entity[1]]
                entity_index = str(i+1) + ': ' + str(entity[0]) + ', ' + str(entity[1])
                self.ent_dict[entity_category][entity_index] = entity_name

    def test_overlapping_indices(self):
        """test no overlapping indices in annotation entity indices"""
        overlapping_index = set()
        for data in TRAIN_DATA:
            # add all entities start/end index to a list
            entity_indices = data[1]["entities"]
            ent_index_list = [(entity[0], entity[1]) for entity in entity_indices]
            # first test all entity have start index smaller than end index
            self.assertTrue(all(entity[0] < entity[1] for entity in ent_index_list))
            # sort the list by start index, for testing overlapping indices
            ent_index_list.sort(key=lambda x: x[0])
            # check if there are overlapping indices, start with the first interval
            # if there is no overlap, update prev_interval to curr_interval
            # if overlap exist, record the overlapping index, and extend current searching(do not update prev_interval),
            # because there might be multiple overlap exist
            prev_interval = ent_index_list[0]
            for curr_interval in ent_index_list[1:]:
                if curr_interval[0] <= prev_interval[1]:
                    overlapping_index.add((prev_interval, curr_interval))
                else:
                    prev_interval = curr_interval
            # output overlapping index, and correct them accordingly
            print(overlapping_index)

    def base_category_test(self, category: str, word_list: list):
        """test annotation word in correct category"""
        if category in self.ent_dict:
            words = set(self.ent_dict[category].values())
            print(category, words)
            for index, word in self.ent_dict[category].items():
                if word not in word_list:
                    print(f'the testing word not in {category} list: {index, word}')
            self.assertTrue(all([word in word_list for word in words]))

    def test_PROGRAMMING_LANGUAGE(self, category='PROGRAMMING_LANGUAGE', word_list=pl_list):
        self.base_category_test(category, word_list)

    def test_OTHER_LANGUAGE(self, category='OTHER_LANGUAGE', word_list=ol_list):
        self.base_category_test(category, word_list)

    def test_LIBRARY(self, category='LIBRARY', word_list=lb_list):
        self.base_category_test(category, word_list)

    def test_FRAMEWORK(self, category='FRAMEWORK', word_list=fw_list):
        self.base_category_test(category, word_list)

    def test_ARCHITECT(self, category='ARCHITECT', word_list=at_list):
        self.base_category_test(category, word_list)

    def test_PROTOCOL(self, category='PROTOCOL', word_list=pt_list):
        self.base_category_test(category, word_list)

    def test_DATA_STORAGE(self, category='DATA_STORAGE', word_list=ds_list):
        self.base_category_test(category, word_list)

    def test_DATA_TRANSMISSION(self, category='DATA_TRANSMISSION', word_list=dt_list):
        self.base_category_test(category, word_list)

    def test_COMPUTER_SCIENCE(self, category='COMPUTER_SCIENCE', word_list=cs_list):
        self.base_category_test(category, word_list)

    def test_AI(self, category='AI', word_list=ai_list):
        self.base_category_test(category, word_list)

    def test_DIVISION(self, category='DIVISION', word_list=dv_list):
        self.base_category_test(category, word_list)

    def test_POSITION(self, category='POSITION', word_list=ps_list):
        self.base_category_test(category, word_list)

    def test_OS(self, category='OS', word_list=os_list):
        self.base_category_test(category, word_list)

    def test_APPROACH(self, category='APPROACH', word_list=ap_list):
        self.base_category_test(category, word_list)

    def test_SOFTWARE_ENGINEERING(self, category='SOFTWARE_ENGINEERING', word_list=se_list):
        self.base_category_test(category, word_list)

    def test_PLATFORM(self, category='PLATFORM', word_list=pf_list):
        self.base_category_test(category, word_list)

    def test_SOFT_SKILL(self, category='SOFT_SKILL', word_list=sf_list):
        self.base_category_test(category, word_list)

    def test_GENERAL(self, category='GENERAL', word_list=ge_list):
        self.base_category_test(category, word_list)

    def test_SOFTWARE_PRODUCT(self, category='CONCEPT', word_list=cp_list):
        self.base_category_test(category, word_list)

    def test_SERVER(self, category='SERVER', word_list=sv_list):
        self.base_category_test(category, word_list)

    def test_TOOL(self, category='TOOL', word_list=tl_list):
        self.base_category_test(category, word_list)

    def test_TEAM(self, category='TEAM', word_list=tm_list):
        self.base_category_test(category, word_list)

    def test_COMPANY(self, category='COMPANY', word_list=cp_list):
        self.base_category_test(category, word_list)

    def test_WORK_EXPERIENCE(self, category='WORK_EXPERIENCE', word_list=we_list):
        self.base_category_test(category, word_list)


if __name__ == '__main__':
    unittest.main()
