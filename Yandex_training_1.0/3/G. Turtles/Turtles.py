def get_max_n_honest_turtles(n_after_and_before):
    N = len(n_after_and_before)
    return len(
        set(
            filter(
                lambda x: all((x[0] + x[1] + 1 == N, x[0] >= 0, x[1] >= 0)),
                n_after_and_before
                )
           )
    )


N = int(input())
n_after_and_before = tuple(tuple(map(int, input().split())) for _ in range(N))
print(get_max_n_honest_turtles(n_after_and_before))
