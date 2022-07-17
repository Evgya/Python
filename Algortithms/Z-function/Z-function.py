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
