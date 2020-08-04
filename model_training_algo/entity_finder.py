"""Annotation util, get a spaCy format annotation for a custom entity"""

import re
from collections import defaultdict

import en_core_web_lg

from constants.constants import CONSTANTS_DICT


def entity_finder(word, text):
    start_index = [m.start() for m in re.finditer(word, text)]
    full_index = [str(i) + ', ' + str(i + len(word)) for i in start_index]
    for index in full_index:
        _type = "None"
        for key, value in CONSTANTS_DICT.items():
            if word in value:
                _type = key
                break
        print('(' + index + ', ' + _type + ')', end=', ')


def get_noun_list(text):
    nlp = en_core_web_lg.load()
    doc = nlp(text)
    return [token.text for token in doc if token.pos_ == 'NOUN']


def print_entities(TRAIN_DATA):

    for index, data in enumerate(TRAIN_DATA):
        ent_dict = defaultdict(list)
        for entity in data[1]["entities"]:
            entity_type = entity[-1]
            entity_name = data[0][entity[0]: entity[1]]
            ent_dict[entity_type].append(entity_name)
        print(f"---------- {index+1} start ----------")
        for key in ent_dict:
            print(key + ':', set(ent_dict[key]))
        print(f"---------- {index+1} end ----------")