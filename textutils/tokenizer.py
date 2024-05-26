# textutils/tokenizer.py

import re

def tokenize(text):
    """
    テキストをトークン化する関数。

    Parameters:
        text (str): トークン化するテキスト。

    Returns:
        list: トークンのリスト。
    """
    # 正規表現を使用して、テキストをトークンに分割する
    tokens = re.findall(r'\w+', text)
    return tokens
