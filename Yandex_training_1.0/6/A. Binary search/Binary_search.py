N, K = map(int, input().split())
first_array = set(map(int,input().split()))
second_array = tuple(map(int,input().split()))
for number in second_array:
    if number in first_array:
        print("YES")
    else:
        print("NO")
