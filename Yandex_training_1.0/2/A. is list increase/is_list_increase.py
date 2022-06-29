def is_list_increase(_list):
<<<<<<< HEAD
    return all((x < y for x, y in zip(_list, _list[1:])))

_list = tuple(map(int, input().split()))
=======
    return all(tuple((x < y for x, y in list(zip(_list, _list[1:])))))

_list = list(map(int, input().split()))
>>>>>>> 6c3e6eb61d5efa85842781f3c52e087dbbf3661c
if is_list_increase(_list):
    print("YES")
else:
    print("NO")
