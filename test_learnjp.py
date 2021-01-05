from learnjp import get_level_word, get_level_words


def test_get_level_word():
    assert get_level_word("使う") == 5
    assert get_level_word("") == 0


def test_get_level_words():
    assert get_level_words(["使う"]) == 5
    assert get_level_words(["使う", "毎朝"]) == 5
    assert get_level_words(["使う", "あくどい"]) == 1
