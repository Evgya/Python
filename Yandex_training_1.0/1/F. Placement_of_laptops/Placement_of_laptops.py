from functools import reduce
laptops_dim = tuple(map(int, input().split()))
S_min = 4*reduce(lambda x, y: max(x, y), laptops_dim)**2 
for i in range(2):
    for j in range(2,4):
        dim1 = laptops_dim[i] + laptops_dim[j]
        dim2 = max(laptops_dim[i + 1 - 2*(i % 2)], laptops_dim[j + 1 - 2*(j % 2)])        
        S = dim1*dim2
        if S < S_min:
            min_dim1 = dim1
            min_dim2 = dim2
            S_min = S 
print(min_dim1, min_dim2)