def get_perimetr_of_cuted_figure(cuted_out_cells, board_dim=8):
    slides = tuple(((-1, 0), (0, -1), (0, 1), (1, 0)))
    chessboard = [[0]*(board_dim + 2) for _ in range(board_dim + 2)]
    for cell in cuted_out_cells:
        chessboard[cell[1]][cell[0]] += 4
        for slide in slides:
            chessboard[cell[1] + slide[1]][cell[0] + slide[0]]-=1
    perimetr = 0
    for y in range(1, board_dim + 1):
        for x in range(1, board_dim + 1):
            if chessboard[y][x] > 0:
                perimetr += chessboard[y][x]
    return perimetr

N = int(input())
cuted_out_cells = set(tuple(map(int, input().split())) for _ in range(N))
print(get_perimetr_of_cuted_figure(cuted_out_cells))
