def get_kth_element(seq, k):
    left_border = 0
    right_border = len(seq) - 1
    while left_border < right_border:
        fst_eq_x = left_border
        fst_gr_x = left_border
        x = seq[(left_border + right_border)//2]
        for idx in range(left_border, right_border + 1):
            if seq[idx] == x:
                seq[idx], seq[fst_gr_x] = seq[fst_gr_x], seq[idx]
                fst_gr_x += 1
            elif seq[idx] < x:
                seq[idx], seq[fst_gr_x] = seq[fst_gr_x], seq[idx]
                seq[fst_eq_x], seq[fst_gr_x] = seq[fst_gr_x], seq[fst_eq_x]
                fst_gr_x += 1
                fst_eq_x += 1
        if fst_eq_x <= k - 1 < fst_gr_x:
            return
        if k <= fst_eq_x:
            right_border = fst_eq_x - 1
        else:
            left_border = fst_gr_x
    return

seq = list(map(int, input().split()))
get_kth_element(seq, len(seq) - 1)
get_kth_element(seq, len(seq) - 3)
get_kth_element(seq, 2)
if seq[0]*seq[1]*seq[-1] > seq[-3]*seq[-2]*seq[-1]:
    print(seq[0], seq[1], seq[-1])
else:
    print(seq[-3], seq[-2], seq[-1])
