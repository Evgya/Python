def get_the_closest_element(_list, x, N):
    val, i = min(
        (val, i) for (i, val) in enumerate(map(lambda y: abs(y - x), _list))
    )
    return((i, _list[i]))

N = int(input())
_list = tuple(map(int, input().split()))
x = int(input())
_, the_closest_element = get_the_closest_element(_list, x, N)
print(the_closest_element)
