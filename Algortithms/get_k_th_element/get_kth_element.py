def get_kth_element(_seq, k, left_border=0, right_border=-1):
    seq = _seq.copy()
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
