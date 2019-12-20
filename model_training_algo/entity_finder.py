import re

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