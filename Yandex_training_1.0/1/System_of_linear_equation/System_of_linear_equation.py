from functools import reduce


def get_rank(system, eps):
    rank = 0
    row_used = [False]*len(system)
    for collumn in range(len(system[0])):
        for row in range(len(system)):
            if abs(system[row][collumn]) > eps and not row_used[row]:
                leader = system[row][collumn]
                system[row] = list(map(lambda x: x/leader, system[row]))
                for i_row in range(0, row):
                    if not row_used[i_row]:
                        system[i_row] = list(
                            map(
                                lambda x, y: x - y*system[i_row][collumn],
                                system[i_row],
                                system[row]
                            )
                        )
                for i_row in range(row + 1, len(system)):
                    if not row_used[i_row]:
                        system[i_row] = list(
                            map(
                                lambda x, y: x - y*system[i_row][collumn],
                                system[i_row],
                                system[row]
                            )
                        )
                row_used[row] = True
                break

    return reduce(
        lambda count, row: count + row,
        map(
            lambda row: reduce(lambda x, y: x + abs(y) > eps, row), system
        )
    )

eps = 1.E-10
a, b, c, d, e, f = (float(input()) for _ in range(6))
system = [[a, b], [c, d]]
system_ext = [[a, b, e], [c, d, f]]
rank = get_rank(system[:], eps)
rank_ext = get_rank(system_ext[:], eps)

if rank != rank_ext:
    print(0)
elif rank == 0:
    print(5)
elif rank == 2:
    x_0 = (e*d - b*f)/(a*d - b*c)
    y_0 = (a*f - e*c)/(a*d - b*c)
    print(2, x_0, y_0)
elif rank == 1:
    if abs(a) > eps:
        if abs(b) > eps:
            print(1, -a/b, e/b)
        else:
            x_0 = e/a
            print(3, x_0)
    elif abs(b) > eps:
        y_0 = e/b
        print(4, y_0)
    elif abs(c) > eps:
        if abs(d) > eps:
            print(1, -c/d, f/d)
        else:
            x_0 = f/c
            print(3, x_0)
    elif abs(d) > eps:
        y_0 = f/d
        print(4, y_0)
