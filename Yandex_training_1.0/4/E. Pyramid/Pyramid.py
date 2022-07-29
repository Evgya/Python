N = int(input())
_dict = dict()
blocks = (map(int, input().split()) for _ in range(N))
for x, y in blocks:
    _dict[x] = max(_dict.setdefault(x, 0), y)
print(sum(_dict.values()))
