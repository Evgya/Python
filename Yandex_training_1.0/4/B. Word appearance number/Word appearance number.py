def get_n_this_word_before(filename="input.txt"):
    _file = open(filename)
    _dict = dict()
    word_before = []
    for word in _file.read().split():
        word_before.append(_dict.get(word, 0))
        _dict.update({word: word_before[-1] + 1})
    _file.close()
    return word_before


print(" ".join(map(str, get_n_this_word_before())))
