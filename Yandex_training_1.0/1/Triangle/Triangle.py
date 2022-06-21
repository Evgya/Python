def is_triangle(a, b, c):
    return all((a + b > c, a + c > b, b + c > a))

a, b, c = tuple(int(input()) for _ in range(3))
if is_triangle(a, b, c):
    print("YES")
else:
    print("NO")
