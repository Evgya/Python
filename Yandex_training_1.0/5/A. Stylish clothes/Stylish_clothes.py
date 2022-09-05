def get_min_difference_pair(A, B):
    i = j = 0
    min_difference_pair = (A[0], B[0])
    min_difference = abs(A[0] - B[0])
    while i != len(A) and j != len(B):
        if A[i] < B[j]:
            if abs(A[i] - B[j]) < min_difference:
                min_difference_pair = (A[i], B[j])
                min_difference = abs(A[i] - B[j])
            i += 1
        elif A[i] == B[j]:
            return (A[i], B[j])
        else:
            if abs(A[i] - B[j]) < min_difference:
                min_difference_pair = (A[i], B[j])
                min_difference = abs(A[i] - B[j])
            j += 1
    if i == len(A):
        if abs(A[-1] - B[j]) < min_difference:
            return (A[-1], B[j])
    else:
        if abs(A[i] - B[-1]) < min_difference:
            return (A[i], B[-1])
    return min_difference_pair


N = int(input())
shirt_colors = tuple(map(int, input().split()))
M = int(input())
pant_colors = tuple(map(int, input().split()))
min_differnce_pair = get_min_difference_pair(shirt_colors, pant_colors)
print(min_differnce_pair[0], min_differnce_pair[1])
