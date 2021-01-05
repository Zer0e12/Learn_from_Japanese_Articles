from collections import defaultdict
from typing import List
import urllib.request

from bs4 import BeautifulSoup


def load_data():
    data = defaultdict(lambda: [])

    with open("jlpt.csv") as f:
        for line in f:
            level, word = line.strip().split(",")
            level = int(level)
            data[level].append(word)

    return data


def verify_data(data):
    unique_words = []
    for word in data.values():
        assert word not in unique_words
        unique_words.append(word)


dictionary = load_data()
verify_data(dictionary)


def get_level_word(word: str) -> int:
    """Returns the level (between 1 and 5) of a word.

    If a word is not found then we return 0.
    """
    for level in dictionary:
        if word in dictionary[level]:
            return level
    return 0


def get_level_words(words: List[str]) -> int:
    """Returns the level (between 1 and 5) of a list of words.
    """
    level = 5
    for word in words:
        word_level = get_level_word(word)
        if word_level != 0:
            level = min(word_level, level)
    return level
