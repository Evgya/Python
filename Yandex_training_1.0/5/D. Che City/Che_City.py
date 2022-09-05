def get_n_ranges_sum_gt_r(D, r):
    i, j = 0, 1
    counter = 0
    while j != len(D):
        if D[j] - D[i] > r:
            counter += len(D) - j
            i += 1
        else:
            j += 1
    return counter

n, r = map(int, input().split())
D = tuple(map(int, input().split()))
print(get_n_ranges_sum_gt_r(D, r))
