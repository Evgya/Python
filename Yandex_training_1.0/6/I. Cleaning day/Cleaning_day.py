def count_crews(heights, C, comfort):
    crew_count = 0
    i = 0
    while i < len(heights) - C + 1:
        if heights[i + C - 1] - heights[i] <= comfort:
            crew_count += 1
            i += C
        else:
            i += 1
    return crew_count


def get_min_discomfort(heights, R, C):
    left_border = 0
    right_border = heights[-1] - heights[0]
    while left_border < right_border:
        middle = (left_border + right_border)//2
        if count_crews(heights, C, middle) >= R:
            right_border = middle
        else:
            left_border = middle + 1
    return left_border

N, R, C = map(int, input().split())
heights = sorted((int(input()) for _ in range(N)))
print(get_min_discomfort(heights, R, C))
