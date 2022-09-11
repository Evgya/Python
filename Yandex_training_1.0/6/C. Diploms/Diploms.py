def get_min_side(w,h,n):
    left_border = max(h, w)
    right_border = n*max(h, w) + 1
    while left_border < right_border:
        middle = (left_border + right_border)//2
        if (middle//h)*(middle//w) >= n:
            right_border = middle
        else:
            left_border = middle + 1
    return left_border

w, h, n = map(int, input().split())
print(min(get_min_side(w,h,n), get_min_side(h,w,n)))
