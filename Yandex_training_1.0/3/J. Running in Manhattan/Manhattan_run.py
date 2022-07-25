def get_rect(center_point, radius):
    return (
        center_point[0] + center_point[1] - radius,
        center_point[0] + center_point[1] + radius,
        center_point[0] - center_point[1] - radius,
        center_point[0] - center_point[1] + radius
    )


def extend_rectangle(rect, t):
    return (rect[0] - t, rect[1] + t, rect[2] - t, rect[3] + t)


def intersect_rectangles(rect_1, rect_2):
    return (
        max(rect_1[0], rect_2[0]),
        min(rect_1[1], rect_2[1]),
        max(rect_1[2], rect_2[2]),
        min(rect_1[3], rect_2[3])
    )


def get_result_rectangle(points, t, d):
    # rect = [min x + y, max x + y, min x - y, max x - y]
    rect = (0, 0, 0, 0)
    for point in points:
        prev_rect = extend_rectangle(rect, t)
        rect = intersect_rectangles(get_rect(point, d), prev_rect)
    return rect


def get_result_int_points(points, t, d):
    rect = get_result_rectangle(points, t, d)
    result_points = []
    for x_plus_y in range(rect[0], rect[1] + 1):
        for x_minus_y in range(rect[2], rect[3] + 1):
            if (x_plus_y + x_minus_y) % 2 == 0:
                x = (x_plus_y + x_minus_y) // 2
                y = x_plus_y - x
                result_points.append((x, y))
    return result_points

t, d, n = map(int, input().split())
points = tuple((tuple(map(int, input().split())) for _ in range(n)))
result_points = get_result_int_points(points, t, d)
print(len(result_points))
for point in result_points:
    print(" ".join(map(str, point)))
