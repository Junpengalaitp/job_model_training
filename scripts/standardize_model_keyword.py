import requests

from database.sql_operation.standard_word import select_all_model_keywords, insert_model_standard_word


def store_model_standard_word():
    df = select_all_model_keywords()
    for word in df.keyword_name.tolist():
        try:
            standard_word = request_standard_word(word)
            insert_model_standard_word(standard_word, word)
        except:
            continue


def request_standard_word(word: str) -> str:
    r = requests.get(f"http://127.0.0.1:8812/standardize-word/{word}")
    if r and r.status_code == 200:
        return r.text


if __name__ == '__main__':
    store_model_standard_word()