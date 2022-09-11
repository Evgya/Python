def round_to_int(numerator, denominator):
    excess = numerator % denominator
    if 2*excess - denominator >= 0:
        return numerator//denominator + 1
    else:
        return numerator//denominator


def count_fives(a, b, c):
    grades_sum = a*2 + b*3 + c*4
    n_grades = a + b + c
    left_border = 0
    right_border = a + b + c
    while left_border < right_border:
        middle = (left_border + right_border)//2
        if round_to_int(grades_sum + middle*5, n_grades + middle) >= 4:
            right_border = middle
        else:
            left_border = middle + 1
    return left_border

a = int(input())
b = int(input())
c = int(input())
print(count_fives(a, b, c))
