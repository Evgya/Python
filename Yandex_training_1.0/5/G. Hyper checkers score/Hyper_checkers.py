def count_n_possible_scores(numbers, k):
    cntnumbers = dict()
    for number in numbers:
        cntnumbers[number] = cntnumbers.setdefault(number, 0) + 1
    sorted_keys = sorted(cntnumbers.keys())
    left_border = right_border = 0
    n_duplicates = 0
    n_possible_scores = 0
    for left_border in range(len(cntnumbers)):
        while (right_border < len(sorted_keys) and
               k*sorted_keys[left_border] >= sorted_keys[right_border]):
            if cntnumbers[sorted_keys[right_border]] >= 2:
                n_duplicates += 1
            right_border += 1

        range_length = right_border - left_border
        if cntnumbers[sorted_keys[left_border]] >= 2:
            n_duplicates -= 1
            n_possible_scores += (range_length - 1)*3
        if cntnumbers[sorted_keys[left_border]] >= 3:
            n_possible_scores += 1
        n_possible_scores += (range_length - 1)*(range_length - 2)*3
        n_possible_scores += n_duplicates*3
    return n_possible_scores

n, k = map(int, input().split())
numbers = tuple(map(int, input().split()))
print(count_n_possible_scores(numbers, k))
