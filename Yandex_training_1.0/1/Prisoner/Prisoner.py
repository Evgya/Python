def is_brick_fit_hole(A, B, C, D, E):
    brick_dims = sorted([A, B, C])
    hole_dims = sorted([D, E])
    if any((brick_dims[0] > hole_dims[0], brick_dims[1] > hole_dims[1])):
        return False
    return True

A, B, C, D, E = (int(input()) for _ in range(5))
if is_brick_fit_hole(A, B, C, D, E):
    print("YES")
else:
    print("NO")
