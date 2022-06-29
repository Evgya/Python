def get_n_elements_bigger_neighbours(_list):
    counter = 0
    for elem in zip(_list, _list[1:], _list[2:]):
        if  all((elem[0] < elem[1], elem[1] > elem[2])):
            counter += 1
    return counter

_list = tuple(map(int,input().split()))
print(get_n_elements_bigger_neighbours(_list))
