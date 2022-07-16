def is_valid_game(game):
    d = {"win1": 0, "win2": 0, "win0": 0, "1": 0, "2": 0, "0": 0}
    for i in range(3):
        d.update([('1', d.get('1', 0) + game[i].count('1'))])
        d.update([('2', d.get('2', 0) + game[i].count('2'))])
        if (game[i][0] == game[i][1] == game[i][2]):
            d.update([("win" + game[i][0], d.get("win" + game[i][0], 0) + 1)])
        if (game[0][i] == game[1][i] == game[2][i]):
            d.update([("win" + game[0][i], d.get("win" + game[0][i], 0) + 1)])
    if (game[0][0] == game[1][1] == game[2][2]):
            d.update([("win" + game[0][0], d.get("win" + game[0][0], 0) + 1)])
    if (game[0][2] == game[1][1] == game[2][0]):
            d.update([("win" + game[0][2], d.get("win" + game[0][2], 0) + 1)])
    if d["win1"] > 0 and d["win2"] > 0:
        return False
    if d["win1"] > 0:
        if d["1"] == d["2"] + 1:
            return True
        else:
            return False
    if d["win2"] > 0:
        if d["1"] == d["2"]:
            return True
        else:
            return False
    if d["1"] == d["2"] + 1 or d["1"] == d["2"]:
        return True
    return False

game = tuple(tuple(input().split()) for _ in range(3))
if is_valid_game(game):
    print("YES")
else:
    print("NO")
