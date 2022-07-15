def get_kth_element(seq, k, left_border=0, right_border=- 1):
    if right_border == -1:
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
        if k <= fst_eq_x:
            right_border = fst_eq_x - 1
        elif k >= fst_gr_x:
            left_border = fst_gr_x
        else:
            return
    return


def get_three_max_product_elements(_seq):
    seq = _seq.copy()
    get_kth_element(seq, len(seq) - 1)
    get_kth_element(seq, len(seq) - 3, 0, len(seq) - 2)
    get_kth_element(seq, 2, 0, len(seq) - 4)
    if seq[0]*seq[1]*seq[-1] > seq[-3]*seq[-2]*seq[-1]:
        return seq[0], seq[1], seq[-1]
    else:
        return seq[-3], seq[-2], seq[-1]

seq = list(map(int, input().split()))
max_product_elem = get_three_max_product_elements(seq)
print(max_product_elem[0], max_product_elem[1], max_product_elem[2])
