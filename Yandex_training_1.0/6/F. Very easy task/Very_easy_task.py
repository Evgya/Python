def get_min_time_to_xerox(N, x, y):
    _min = min(x, y)
    left_border = 0
    right_border = _min*N
    while left_border < right_border:
        middle = (left_border + right_border)//2
        if middle//x + middle//y >= N - 1:
            right_border = middle
        else:
            left_border = middle + 1
    return left_border + _min

N, x, y = map(int, input().split())
print(get_min_time_to_xerox(N, x, y))
