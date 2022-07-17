import math


def get_n_watered_and_clipped(x1, y1, x2, y2, x3, y3, R):
    left_y = max(y1, y3 - R)
    right_y = min(y2, y3 + R)
    counter = 0
    for y in range(left_y, right_y + 1):
        tmp = (R**2 - (y - y3)**2)**(1/2)
        left_x = max(math.ceil(x3 - tmp), x1)
        right_x = min(math.floor(x3 + tmp), x2)
        if (right_x >= left_x):
            counter += right_x - left_x + 1
    return counter

x1, y1, x2, y2 = map(int, input().split())
x3, y3, R = map(int, input().split())
print(get_n_watered_and_clipped(x1, y1, x2, y2, x3, y3, R))
