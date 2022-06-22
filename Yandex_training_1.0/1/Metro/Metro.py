def get_min_max_waiting_time(a, b, n, m):
    min_max_times = [
                a*(n - 1) + n,
                a*(n + 1) + n,
                b*(m - 1) + m,
                b*(m + 1) + m
                ]
    if any(
        (min_max_times[1] < min_max_times[2],
         min_max_times[3] < min_max_times[0])):
        return -1, -1
    min_max_times.sort()
    return min_max_times[1], min_max_times[2]

a, b, n, m = (int(input()) for _ in range(4))
min_time, max_time = get_min_max_waiting_time(a, b, n, m)
if min_time == -1:
    print(min_time)
else:
    print(min_time, max_time)
