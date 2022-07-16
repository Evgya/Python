def is_triangle(a, b, c):
    return all((a + b > c, a + c > b, b + c > a))


def find_max_square_triangle(p):
    a_max = p//3
    b_max = (p - a_max)//2
    c_max = p - a_max - b_max
    if is_triangle(a_max, b_max, c_max):
        return a_max, b_max, c_max
    else:
        return -1, -1, -1


def find_min_square_triangle(p):
    a_min = b_min = (p - 1) // 2
    c_min = p - a_min - b_min
    if is_triangle(a_min, b_min, c_min):
        return a_min, b_min, c_min
    else:
        return -1, -1, -1

p = int(input())
a_max, b_max, c_max = find_max_square_triangle(p)
if a_max == -1:
    print(-1)
else:
    print(a_max, b_max, c_max)
    a_min, b_min, c_min = find_min_square_triangle(p)
    if a_min == -1:
        print(a_max, b_max, c_max)
    else:
        print(a_min, b_min, c_min)
