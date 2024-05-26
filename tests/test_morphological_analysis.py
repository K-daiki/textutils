# tests/test_morphological_analysis.py

import unittest
from textutils.morphological_analysis import analyze_morphology

class TestMorphologicalAnalysis(unittest.TestCase):
    def test_analyze_morphology(self):
        text = "今日はいい天気ですね。"
        expected_analysis = [('今日', '名詞', '今日'), ('は', '助詞', 'は'), ('いい', '形容詞', 'いい'), ('天気', '名詞', '天気'), ('です', '助動詞', 'です'), ('ね', '助詞', 'ね'), ('。', '記号', '。')]
        analysis_result = analyze_morphology(text)
        self.assertEqual(analysis_result, expected_analysis)

if __name__ == '__main__':
    unittest.main()
