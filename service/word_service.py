from constants.constants import CATEGORY_MAP
from database.sql_operation.standard_word import insert_standard_words, update_stand_words, select_standard_words


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


if __name__ == '__main__':
    store_all_categories()
