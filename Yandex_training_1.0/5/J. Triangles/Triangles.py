def get_n_iso_triangles(points):
    n_triangles = 0
    for i in range(len(points)):
        used_points = set()
        len_count = {}
        for j in range(len(points)):
            x = points[i][0] - points[j][0]
            y = points[i][1] - points[j][1]
            length = x*x + y*y
            len_count[length] = len_count.setdefault(length, 0) + 1
            if (x, y) in used_points:
                n_triangles -= 1
            used_points.add((-x, -y))
        n_triangles += sum(map(lambda n: ((n - 1)*n)//2, len_count.values()))
    return n_triangles

n = int(input())
points = tuple((tuple(map(int, input().split())) for _ in range(n)))
print(get_n_iso_triangles(points))
