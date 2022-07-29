N = int(input())
_dict = dict(input().split() for _ in range(N))
_dict.update({val: key for key, val in _dict.items()})
print(_dict[input()])
