END_SEQUENCE = -2000000000
seq_types = {
    "CONSTANT": lambda x, y: x == y,
    "ASCENDING": lambda x, y: x > y,
    "WEAKLY ASCENDING": lambda x, y: x >= y,
    "DESCENDING": lambda x, y: x < y,
    "WEAKLY DESCENDING": lambda x, y: x <= y
}

previous_element, current_element = map(int,(input(), input()))
while(current_element != END_SEQUENCE):
    seq_types = dict(
        filter(
            lambda f: f[1](current_element, previous_element),
            seq_types.items()
        )
    )
    previous_element = current_element
    current_element = int(input())

if len(seq_types) == 0:
    print("RANDOM")
elif len(seq_types) == 1:
    print("".join(seq_types.keys()))
elif len(seq_types) == 2:
    if "ASCENDING" in seq_types.keys():
        print("ASCENDING")
    else:
        print("DESCENDING")
else:
    print("CONSTANT")
