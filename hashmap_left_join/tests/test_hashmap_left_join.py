from  hashmap_left_join import left_join, Hashmap

def test_left_join():
    hash1 = Hashmap()
    hash1.put('diligent', 'employed')
    hash1.put('fond', 'enamored')
    hash1.put('guide', 'usher')
    hash1.put('outfit', 'garb')
    hash1.put('wrath', 'anger')

    hash2 = Hashmap()
    hash2.put('diligent', 'idle')
    hash2.put('fond', 'averse')
    hash2.put('guide', 'follow')
    hash2.put('flow', 'jam')
    hash2.put('wrath', 'delight')

    result = left_join(hash1, hash2)

    expected_result = [
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['outfit', 'garb', None],
        ['wrath', 'anger', 'delight']
    ]

    assert result == expected_result
