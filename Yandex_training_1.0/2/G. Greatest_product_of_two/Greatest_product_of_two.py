def get_nums_with_max_product(numbers):
    min_1 = max_2 = min(numbers[0], numbers[1])
    max_1 = min_2 = max(numbers[0], numbers[1])

    for number in numbers[2:]:
        if number > max_1:
            max_2 = max_1
            max_1 = number
        elif number > max_2:
            max_2 = number

        if number < min_1:
            min_2 = min_1
            min_1 = number
        elif number < min_2:
            min_2 = number

    if min_1*min_2 > max_1*max_2:
        return min(min_1, min_2), max(min_1, min_2)
    else:
        return min(max_1, max_2), max(max_1, max_2)

numbers = tuple(map(int, input().split()))
answer = get_nums_with_max_product(numbers)
print(answer[0], answer[1])
