def get_prefix_sum(_list):
    prefix_sum = [0] * (len(_list) + 1)
    for i in range(len(_list)):
        prefix_sum[i + 1] = prefix_sum[i] + _list[i]
    return prefix_sum


def get_n_ranges_sum_eq_k(car_numbers, K):
    i, j = 0, 1
    counter = 0
    prefix_sum = get_prefix_sum(car_numbers)
    while i != len(prefix_sum) and j != len(prefix_sum):
        if prefix_sum[j] - prefix_sum[i] == K:
            counter += 1
            i += 1
            j += 1
        elif prefix_sum[j] - prefix_sum[i] > K:
            i += 1
        else:
            j += 1
    return counter

N, K = map(int, input().split())
car_numbers = tuple(map(int, input().split()))
print(get_n_ranges_sum_eq_k(car_numbers, K))
