def calc_z_function(string, N):
    z = [0] * N
    left, right = 0, 0
    for i in range(N):
        z[i] = max(0, min(z[i - left], right - i))
        # change next line to get z-function
        # while i + z[i] < N and s[z[i]] == s[i + z[i]]:
        while i + z[i] < N and string[-z[i] - 1] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def get_missing_symbols_to_palindrome(string, N):
    z = calc_z_function(string, N)
    for i in range(N):
        if i + z[i] == N:
            return i, string[0:i][::-1]

N = int(input())
string = input().replace(" ", "")

M, missing_symbols = get_missing_symbols_to_palindrome(string, N)
print(M)
if M != 0:
    print(" ".join(missing_symbols))
