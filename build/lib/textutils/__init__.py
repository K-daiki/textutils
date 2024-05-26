# textutils/__init__.py

# パッケージのバージョンを定義する
__version__ = "0.1.0"

# パッケージの公開APIを定義する
from .tokenizer import tokenize
from .counter import count_words
from .morphological_analysis import analyze_morphology
