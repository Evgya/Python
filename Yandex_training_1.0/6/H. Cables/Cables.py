def get_min_length_K_pieces(lengths, K):
    right_border = sum(lengths)
    if right_border < K:
        return 0
    right_border //= K
    left_border = 1
    while left_border < right_border:
        middle = (left_border + right_border + 1)//2
        if sum(map(lambda x: x//middle, lengths)) >= K:
            left_border = middle
        else:
            right_border = middle - 1
    return left_border

N, K = map(int, input().split())
lengths = tuple((int(input()) for _ in range(N)))
print(get_min_length_K_pieces(lengths, K))
