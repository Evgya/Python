def get_max_width(n, m, t):
    left_border = 0
    right_border = min(n, m)//2
    while left_border < right_border:
        width = (left_border + right_border + 1)//2
        if n*m - (n - 2*width)*(m - 2*width) <= t:
            left_border = width
        else:
            right_border = width - 1
    return left_border

n = int(input())
m = int(input())
t = int(input())
print(get_max_width(n, m, t))
