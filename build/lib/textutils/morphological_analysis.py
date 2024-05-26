# textutils/morphological_analysis.py

import MeCab

def analyze_morphology(text):
    """
    テキストの形態素解析を行う関数。

    Parameters:
        text (str): 形態素解析を行うテキスト。

    Returns:
        list: 形態素解析結果のリスト。各要素はタプルで、(表層形, 品詞, 原形)を含む。
    """
    # MeCabを使用してテキストを形態素解析する
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)

    # 解析結果を格納するリスト
    result = []
    while node:
        surface = node.surface
        feature = node.feature.split(',')
        # 表層形、品詞、原形をタプルとしてリストに追加
        result.append((surface, feature[0], feature[6]))
        node = node.next
    return result
