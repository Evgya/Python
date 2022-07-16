from functools import reduce


def diff_max_min_after_k_confuse(B, K):
    _min = reduce(lambda x, y: min(x, y), B)
    _max = reduce(lambda x, y: max(x, y), B)
    return _max - _min

N, K = map(int, input().split())
B = tuple(map(int, input().split()))
print(diff_max_min_after_k_confuse(B, K))
