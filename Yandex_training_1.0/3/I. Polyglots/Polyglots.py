from functools import reduce


def get_generaly_known_langs(langs):
    return reduce(lambda x, y: x & y, langs)


def get_all_known_langs(langs):
    return reduce(lambda x, y: x | y, langs)


N = int(input())
langs = []
for _ in range(N):
    M = int(input())
    langs.append(set(input() for _ in range(M)))

generaly_known_langs = get_generaly_known_langs(langs)
print(len(generaly_known_langs))
for lang in generaly_known_langs:
    print(lang)

all_known_langs = get_all_known_langs(langs)
print(len(all_known_langs))
for lang in all_known_langs:
    print(lang)
