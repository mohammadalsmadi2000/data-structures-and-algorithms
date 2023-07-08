import pytest
from hashmap_left_join import left_join

@pytest.fixture
def synonyms():
    return {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger"
    }

@pytest.fixture
def antonyms():
    return {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight"
    }

def test_left_join(synonyms, antonyms):
    result = left_join(synonyms, antonyms)
    assert result == [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['outfit', 'garb', None],
        ['wrath', 'anger', 'delight']
    ]

def test_left_join_with_empty_hashmap(synonyms):
    empty_hashmap = {}
    result = left_join(synonyms, empty_hashmap)
    assert result == [
        ['diligent', 'employed', None],
        ['fond', 'enamored', None],
        ['guide', 'usher', None],
        ['outfit', 'garb', None],
        ['wrath', 'anger', None]
    ]

def test_left_join_with_missing_keys(antonyms):
    missing_keys_hashmap = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "unknown": "word"
    }
    result = left_join(missing_keys_hashmap, antonyms)
    assert result == [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['unknown', 'word', None]
    ]
