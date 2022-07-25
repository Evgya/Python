def get_n_buttons_to_add(xyz, N):
    return len(set(N) - set(xyz))


print(get_n_buttons_to_add(input().split(), input()))
