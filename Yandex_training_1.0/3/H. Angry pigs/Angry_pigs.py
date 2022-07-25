def get_min_n_shots(points):
    return len(set(map(lambda x: x[0], points)))


N = int(input())
points = tuple(tuple(map(int, input().split())) for _ in range(N))
print(get_min_n_shots(points))
