n = int(input())
C = list(map(int, input().split()))
k = int(input())
P = tuple(map(int, input().split()))
_dict = dict()
for button in P:
    _dict.update({button: _dict.get(button, 0) + 1})
for idx in range(1, n + 1):
    if C[idx - 1] - _dict.get(idx, 0) < 0:
        print("YES")
    else:
        print("NO")
