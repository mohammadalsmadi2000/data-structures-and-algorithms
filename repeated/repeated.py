def repeated(string):
    words = string.split()
    word_count = {}
    for word in words:
        word = word.strip(".,!?;:")
        word = word.lower()
        if word in word_count:
            return word
        else:
            word_count[word] = 1
    return ""
