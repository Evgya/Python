def count_greater(x, _list):
    return len(_list) - count_less(x + 1, _list)


def count_less(x, _list):
    left_border = 0
    right_border = len(_list) - 1
    while left_border < right_border:
        middle = (left_border + right_border)//2
        if _list[middle] >= x:
            right_border = middle
        else:
            left_border = middle + 1
    if _list[left_border] < x:
        return len(_list)
    return left_border


def get_median_of_merge(seq1, seq2):
    left_border = min(seq1[0], seq2[0])
    right_border = max(seq1[-1], seq2[-1])
    while left_border < right_border:
        mid = (left_border + right_border)//2
        less_mid = count_less(mid, seq1) + count_less(mid, seq2)
        greater_mid = count_greater(mid, seq1) + count_greater(mid, seq2)
        if less_mid <= len(seq1) - 1 and greater_mid <= len(seq1):
            return mid
        if greater_mid > len(seq1):
            left_border = mid + 1
        if less_mid > len(seq1) - 1:
            right_border = mid - 1
    return left_border


N, L = map(int, input().split())
sequences = []
for _ in range(N):
    sequences.append(tuple(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        print(get_median_of_merge(sequences[i], sequences[j]))
