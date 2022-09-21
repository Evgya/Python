def is_time_table_valid(timetable, N):
    balance = [0]*(N + 1)
    for trip in timetable:
        balance[trip[0]] += 1
        balance[trip[2]] -= 1
    return all(map(lambda x: x == 0, balance))


def count_min_buses(timetable):
    ARRIVED, LEFT = -1, 1
    buses_in_cities = [0]*(N + 1)
    events = [0]*2*len(timetable)
    j = 0
    for i in range(0, len(events) - 1, 2):
        events[i] = (timetable[j][1], LEFT, timetable[j][0])
        events[i + 1] = (timetable[j][3], ARRIVED, timetable[j][2])
        j += 1
    events.sort()
    for event in events:
        if event[1] == ARRIVED:
            buses_in_cities[event[2]] += 1
        elif event[1] == LEFT and buses_in_cities[event[2]] != 0:
            buses_in_cities[event[2]] -= 1
    return sum(map(lambda x: x[3] < x[1], timetable)) + sum(buses_in_cities)

N, M = map(int, input().split())
timetable = [0]*M
for i in range(M):
    _input = input().split()
    _input[1] = int(_input[1][0:2])*60 + int(_input[1][3:])
    _input[3] = int(_input[3][0:2])*60 + int(_input[3][3:])
    timetable[i] = tuple(map(int, _input))
if is_time_table_valid(timetable, N):
    print(count_min_buses(timetable))
else:
    print("-1")
