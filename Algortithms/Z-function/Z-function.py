def calc_z_function(string, N):
    z = [0] * N
    left, right = 0, 0
    for i in range(N):
        z[i] = max(0, min(z[i - left], right - i))
        while i + z[i] < N and string[z[i]] == string[i + z[i]]:        
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z
