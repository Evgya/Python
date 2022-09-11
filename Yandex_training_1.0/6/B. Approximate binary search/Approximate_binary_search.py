def bin_search(x, _list):
    left_border = 0
    right_border = len(_list) - 1
    while left_border < right_border:
        middle = (right_border + left_border)//2
        if _list[middle] >= x:
            right_border = middle
        else:
            left_border = middle + 1
    return left_border

N, K = map(int, input().split())
sorted_array = tuple(map(int, input().split()))
array = tuple(map(int, input().split()))
for number in array:
    i = bin_search(number, sorted_array)
    if i == 0:
        print(sorted_array[0])
    elif abs(sorted_array[i - 1] - number) > abs(sorted_array[i] - number):
        print(sorted_array[i])
    else:
        print(sorted_array[i - 1])
