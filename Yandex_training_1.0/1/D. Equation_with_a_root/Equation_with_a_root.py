def solve_in_int(a, b, c):
    if (c < 0):
        return "NO SOLUTION"
    if (a == 0):
        if (c*c == b):
            return "MANY SOLUTIONS"
        return "NO SOLUTION"
    else:
        x = (c*c - b)/a
        if x.is_integer():
            return int(x)
        return "NO SOLUTION"

a, b, c = (int(input()) for _ in range(3))
print (solve_in_int(a, b, c))
