
def find_minmax_frequency(
                      prev_measure,
                      measuring,
                      left_border=30,
                      right_border=4000
                      ):
    for measure in measuring:
        if measure[1] == "closer":
            if measure[0] > prev_measure:
                left_border = max(left_border, (measure[0] + prev_measure)/2)
            else:
                right_border = min(right_border, (measure[0] + prev_measure)/2)
        else:
            if measure[0] > prev_measure:
                right_border = min(right_border, (measure[0] + prev_measure)/2)
            else:
                left_border = max(left_border, (measure[0] + prev_measure)/2)
        prev_measure = measure[0]
    return left_border, right_border


n = int(input())
first_measure = float(input())
measuring = []
for _ in range(n - 1):
    measure = input().split()
    measuring.append((float(measure[0]), measure[1]))
min_frequency, max_frequency = find_minmax_frequency(first_measure, measuring)
print(min_frequency, max_frequency)
