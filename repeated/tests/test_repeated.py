from repeated import repeated

def test_repeated_word_first_repeated():
    string = "Once upon a time, there was a brave princess who..."
    assert repeated(string) == "a"

def test_repeated_word_no_repeated():
    string = "It was the best of times, it was the worst of times..."
    assert repeated(string) == "it"

def test_repeated_case_insensitivity():
    string = "It was a queer, sultry summer, the Summer they electrocuted the Rosenbergs..."
    assert repeated(string) == "summer"