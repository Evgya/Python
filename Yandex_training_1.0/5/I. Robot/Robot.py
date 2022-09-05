def get_efficient_uses(K, operations):
    previous_len = efficient_uses = 0
    for i in range(K, len(operations)):
        if operations[i] == operations[i - K]:
            previous_len += 1
            efficient_uses += previous_len
        else:
            previous_len = 0
    return efficient_uses

K = int(input())
operations = input()
print(get_efficient_uses(K, operations))
