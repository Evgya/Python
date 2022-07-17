from functools import reduce


def calc_min_length_of_rope(lengths):
    _max = max(lengths)
    sum_of_lengths = sum(lengths)
    if _max > sum_of_lengths - _max:
        return 2*_max - sum_of_lengths
    else:
        return sum_of_lengths

N = int(input())
l = tuple(map(int, input().split()))
print(calc_min_length_of_rope(l))
