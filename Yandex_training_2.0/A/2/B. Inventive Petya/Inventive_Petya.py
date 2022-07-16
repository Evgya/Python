def calc_z_function(string):
    z = [0] * len(string)
    left, right = 0, 0
    for i in range(1, len(string)):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < len(string) and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def get_Y(X, Z):
    ZX = Z + "#" + X*(len(Z)//len(X) + 1)
    z_func = calc_z_function(ZX)
    for i in range(len(Z) + 1, len(ZX)):
        if i + z_func[i] == len(ZX):
            return Z[z_func[i]:]
    return Z

X = input()
Z = input()
print(get_Y(X, Z))
