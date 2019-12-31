from constants.constants import CATEGORY_MAP
from database.sql_operation.standard_word import insert_standard_words, update_stand_words, select_standard_words, \
    select_all_standard_words, delete_stand_word


def store_standard_words(collection: dict, category: str):
    for standard_word, other_words in collection.items():
        df = select_standard_words(standard_word)
        other_words = ','.join(other_words)
        if df.empty:
            insert_standard_words(standard_word, other_words, category)
        elif df['other_words'][0] != other_words:
            update_stand_words(standard_word, other_words)


def store_all_categories():
    for category, collection in CATEGORY_MAP.items():
        store_standard_words(collection, category)
    delete_standard_words()


def delete_standard_words():
    df = select_all_standard_words()
    all_standard_words = []
    for category, collection in CATEGORY_MAP.items():
        for standard_word in collection.keys():
            all_standard_words.append(standard_word)
    unwanted_standard_words = set(df['standard_word'].tolist()) - set(all_standard_words)
    for word in unwanted_standard_words:
        delete_stand_word(word)


if __name__ == '__main__':
    store_all_categories()
