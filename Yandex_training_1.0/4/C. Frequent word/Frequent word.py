def get_n_every_word(filename="input.txt"):
    _file = open(filename)
    _dict = dict()
    word_before = []
    for word in _file.read().split():
        word_before.append(_dict.get(word, 0))
        _dict.update({word: word_before[-1] + 1})
    _file.close()
    return _dict


def get_max_n_word(filename="input.txt"):
    _dict = get_n_every_word(filename)
    max_n = max(_dict.values())
    return min(tuple(filter(lambda x: _dict[x] == max_n, _dict.keys())))

print(get_max_n_word())
