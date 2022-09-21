def find_best_time_for_advertisments(customers, adv_len=5):
    events = []
    IN, OUT = -1, 1
    max_customers = 0
    i = 0
    for customer in filter(lambda x: x[1] - x[0] >= adv_len, customers):
        events.append((customer[0], IN, i))
        events.append((customer[1] - adv_len, OUT, i))
        i += 1

    if len(events) == 0:
        return 0, adv_len, 2*adv_len
    if len(events) == 2:
        return 1, events[0][0], events[0][0] + 2*adv_len
    events.sort()

    first_adv = set()
    for i in range(len(events)):
        if events[i][1] == IN:
            first_adv.add(events[i][2])
        if len(first_adv) > max_customers:
            max_customers = len(first_adv)
            best_time_for_1st_adv = events[i][0]
            best_time_for_2nd_adv = events[i][0] + 2*adv_len
        second_adv = 0
        for j in range(i + 1, len(events)):
            if events[j][1] == IN and events[j][2] not in first_adv:
                second_adv += 1
            if all(
                (
                    len(first_adv) + second_adv > max_customers,
                    events[j][0] - adv_len >= events[i][0]
                )
            ):
                max_customers = len(first_adv) + second_adv
                best_time_for_1st_adv = events[i][0]
                best_time_for_2nd_adv = events[j][0]
            if events[j][1] == OUT and events[j][2] not in first_adv:
                second_adv -= 1
        if events[i][1] == OUT:
            first_adv.remove(events[i][2])
    return max_customers, best_time_for_1st_adv, best_time_for_2nd_adv

N = int(input())
customers = tuple((tuple(map(int, input().split())) for _ in range(N)))
print(" ".join(map(str, find_best_time_for_advertisments(customers))))
