def get_max_layer(n, a, b, w, h):
    left_border = 0
    right_border = max(w, h)
    while left_border < right_border:
        d = (left_border + right_border + 1)//2
        if (w//(a + 2*d))*(h//(b + 2*d)) >= n:
            left_border = d
        else:
            right_border = d - 1
    return left_border

n, a, b, w, h = map(int, input().split())
print(max(get_max_layer(n, a, b, w, h), get_max_layer(n, b, a, w, h)))
