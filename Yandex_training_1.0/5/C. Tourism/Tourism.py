def get_prefix_sum(_list):
    prefix_sum = [0] * (len(_list) + 1)
    for i in range(len(_list)):
        prefix_sum[i + 1] = prefix_sum[i] + _list[i]
    return prefix_sum

N = int(input())
points = tuple(
    (tuple(map(int, input().split())) for _ in range(N))
    )
climbs_and_descents = tuple(
    (points[i][1] - points[i - 1][1] for i in range(1, len(points)))
    )

climbs = tuple((map(lambda x: (x + abs(x))//2, climbs_and_descents)))
descents = tuple((map(lambda x: (x - abs(x))//2, climbs_and_descents)))
climb_prefix_sum = get_prefix_sum(climbs)
descent_prefix_sum = get_prefix_sum(descents)
M = int(input())
for _ in range(M):
    route_begin, route_end = map(lambda x: int(x) - 1, input().split())
    if route_begin < route_end:
        print(
            climb_prefix_sum[route_end] - climb_prefix_sum[route_begin]
            )
    else:
        print(
            descent_prefix_sum[route_end] - descent_prefix_sum[route_begin]
            )
