import pytest
from hash import Hashtable

@pytest.fixture
def hashtable():
    return Hashtable()

def test_set_and_get(hashtable):
    hashtable.set("key1", "value1")
    assert hashtable.get("key1") == "value1"

def test_get_nonexistent_key(hashtable):
    assert hashtable.get("nonexistent") is None

def test_has(hashtable):
    hashtable.set("key1", "value1")
    assert hashtable.has("key1") is True
    assert hashtable.has("nonexistent") is False

def test_keys(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    assert hashtable.keys() == ["key1", "key2"]

def test_collision(hashtable):

    hashtable.set("key1", "value1")
    hashtable.set("akey", "value2")

    assert hashtable.get("key1") == "value1"
    assert hashtable.get("akey") == "value2"

def test_hash_range(hashtable):

    for i in range(1000):
        key = f"key{i}"
        hash_value = hashtable.hash(key)
        assert 0 <= hash_value < hashtable.size
