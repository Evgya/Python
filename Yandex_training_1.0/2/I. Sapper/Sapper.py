def get_field(bombs_cords, N, M):
    field = []
    slides = tuple(
        ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    )
    _field = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

    for bomb_cords in bombs_cords:
        for slide in slides:
            _field[bomb_cords[0] + slide[0]][bomb_cords[1] + slide[1]] += 1

    for bomb_cords in bombs_cords:
        _field[bomb_cords[0]][bomb_cords[1]] = "*"

    for line in _field[1:N + 1]:
        field.append(" ".join(map(str, line[1:M + 1])))
    return field

N, M, K = map(int, input().split())
bombs_cords = tuple(tuple(map(int, input().split())) for _ in range(K))
for line in get_field(bombs_cords, N, M):
    print(line)
