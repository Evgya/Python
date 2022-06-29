def is_list_increase(_list):
    return all(tuple((x < y for x, y in list(zip(_list, _list[1:])))))

_list = list(map(int, input().split()))
if is_list_increase(_list):
    print("YES")
else:
    print("NO")
