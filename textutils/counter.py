# textutils/counter.py

from collections import Counter
from .tokenizer import tokenize

def count_words(text):
    """
    テキスト内の単語の出現回数をカウントする関数。

    Parameters:
        text (str): 単語の出現回数をカウントするテキスト。

    Returns:
        dict: 単語をキーとし、出現回数を値とする辞書。
    """
    # テキストをトークン化する
    tokens = tokenize(text)
    # 単語の出現回数をカウントする
    word_count = Counter(tokens)
    return word_count
