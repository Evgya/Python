def get_n_words_in_text(filename="input.txt"):
    _file = open(filename)
    n_words = len(set(_file.read().split()))
    _file.close()
    return n_words


print(get_n_words_in_text())
