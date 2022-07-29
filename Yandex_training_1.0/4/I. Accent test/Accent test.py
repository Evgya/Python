def count_errors(_dict, exercise):
    counter = 0
    for word in exercise:
        key = word.lower()
        if any(
            (
                sum(map(lambda x: x.isupper(), word)) != 1,
                key in _dict and word not in _dict[key]
            )
        ):
            counter += 1
    return counter


N = int(input())
_dict = dict()
for _ in range(N):
    word = input()
    _dict.setdefault(word.lower(), []).append(word)
exercise = input().split()
print(count_errors(_dict, exercise))
