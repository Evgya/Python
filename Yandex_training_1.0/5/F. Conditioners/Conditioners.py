def get_min_price(conditioners, min_capacites):
    reverse_dict = dict()
    for capacity, price in conditioners.items():
        reverse_dict[price] = max(
            reverse_dict.setdefault(price, capacity), capacity
            )
    conditioners = {
        capacity: price for price, capacity in reverse_dict.items()
        }
    capacites = sorted(conditioners.keys())
    prices = sorted(conditioners.values())
    benefic_conditioners = []
    i = j = 0
    while j < len(capacites):
        if conditioners[capacites[j]] == prices[i]:
            benefic_conditioners.append(capacites[j])
            i += 1
            j += 1
        elif reverse_dict[prices[i]] == - 1:
            i += 1
        else:
            reverse_dict[conditioners[capacites[j]]] = -1
            j += 1
    i = j = 0
    total = 0
    while i < len(min_capacites):
        if benefic_conditioners[j] >= min_capacites[i]:
            total += conditioners[benefic_conditioners[j]]
            i += 1
        else:
            j += 1
    return total

n = int(input())
min_capacites = sorted(map(int, input().split()))
m = int(input())
conditioners = dict()
for _ in range(m):
    capacity, price = map(int, input().split())
    conditioners[capacity] = min(
        conditioners.setdefault(capacity, price), price
        )

print(get_min_price(conditioners, min_capacites))
