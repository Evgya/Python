def is_parallelogram(points):
    middle_points = set()
    for i in range(0, len(points), 2):
        for j in range(i + 2, len(points), 2):
            if points[i] == points[j] and points[i + 1] == points[j + 1]:
                return False
            middle_point = tuple(
                       (points[i] + points[j], points[i + 1] + points[j + 1]))
            middle_points.add(middle_point)
    if len(middle_points) == 5:
        return True
    return False

N = int(input())
for i in range(N):
    points = tuple(map(int, input().split()))
    if is_parallelogram(points):
        print ("YES")
    else:
        print("NO")
