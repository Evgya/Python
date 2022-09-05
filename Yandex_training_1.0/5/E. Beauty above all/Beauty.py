def get_min_range_with_k_sorts(tree_kinds, N, K):
    _dict = {tree_kinds[0]: 1}
    sorts_in_range = 1
    left_border, right_border = 0, N - 1
    i = j = 0
    min_length = N
    while i <= j:
        while sorts_in_range != K and j != N - 1:
            j += 1
            _dict[tree_kinds[j]] = _dict.setdefault(tree_kinds[j], 0) + 1
            if _dict[tree_kinds[j]] == 1:
                sorts_in_range += 1

        if sorts_in_range == K:
            if j - i + 1 < min_length:
                left_border = i
                right_border = j
                min_length = j - i + 1

        _dict[tree_kinds[i]] -= 1
        if _dict[tree_kinds[i]] == 0:
            sorts_in_range -= 1
        i += 1
    return left_border + 1, right_border + 1

N, K = map(int, input().split())
tree_kinds = tuple(input().split())
min_range_with_k_sorts = get_min_range_with_k_sorts(tree_kinds, N, K)
print (min_range_with_k_sorts[0], min_range_with_k_sorts[1])
