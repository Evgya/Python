def get_time_all_open(ticket_offices):
    events = []
    OPEN, CLOSE = -1, 1
    count_opens = 0
    begin = end = (0, 0)
    all_open_time = 0
    for office in ticket_offices:
        if office[0:2] > office[2:4]:
            events.append(((0, 0), OPEN))
            events.append(((office[2], office[3]), CLOSE))
            events.append(((office[0], office[1]), OPEN))
            events.append(((24, 0), CLOSE))
        elif office[0: 2] == office[2: 4]:
            events.append(((0, 0), OPEN))
            events.append(((24, 0), CLOSE))
        else:
            events.append(((office[0], office[1]), OPEN))
            events.append(((office[2], office[3]), CLOSE))
    events.sort()
    for event in events:
        if event[1] == OPEN:
            count_opens += 1
            begin = event[0]
        if event[1] == CLOSE:
            if count_opens == len(ticket_offices):
                end = event[0]
                all_open_time += (end[0] - begin[0])*60 + (end[1] - begin[1])
            count_opens -= 1
    return all_open_time

N = int(input())
ticket_offices = tuple((tuple(map(int, input().split())) for _ in range(N)))
print(get_time_all_open(ticket_offices))
