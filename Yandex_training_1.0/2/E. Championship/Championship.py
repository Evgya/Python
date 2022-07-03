def get_max_place(ranges_of_throw, N, end_of_range):
    ranges_of_throw_sorted = sorted(ranges_of_throw, reverse=True)
    winner_range = ranges_of_throw_sorted[0]
    max_range = -1
    is_winner_acted = False
    for idx in range(0, N - 1):
        if all((
            ranges_of_throw[idx] % 10 == end_of_range,
            ranges_of_throw[idx + 1] < ranges_of_throw[idx],
            is_winner_acted,
            ranges_of_throw[idx] > max_range
        )):
            max_range = ranges_of_throw[idx]
        if ranges_of_throw[idx] == winner_range:
            is_winner_acted = True
    if max_range == -1:
        return 0
    return ranges_of_throw_sorted.index(max_range) + 1

N = int(input())
ranges_of_throw = tuple(map(int, input().split()))
print (get_max_place(ranges_of_throw, N, 5))
