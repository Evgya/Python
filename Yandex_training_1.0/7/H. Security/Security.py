def can_be_one_removed(watches_times, day_end=10000):
    IN, OUT = -1, 1
    events = [0]*2*len(watches_times)
    j = 0
    for i in range(1, len(events), 2):
        events[i - 1] = (watches_times[j][0], IN, j)
        events[i] = (watches_times[j][1], OUT, j)
        j += 1
    events.sort()   
    if events[-1][0] != day_end or events[0][0] != 0:        
        return "Wrong Answer"
    cur_sec = set([events[0][2]])
    cant_be_removed = set()
    prev_event = events[0][0]
    for event in events[1::]:
        if event[0] != prev_event and len(cur_sec) == 1:
            cant_be_removed.update(cur_sec) 
        if len(cur_sec) == 0:            
            return "Wrong Answer"
        if event[1] == IN:
            cur_sec.add(event[2])            
        else:
            cur_sec.remove(event[2])
        prev_event = event[0]   
    if len(cant_be_removed) == len(watches_times):
        return "Accepted"
    else:
        return "Wrong Answer"

K = int(input())
for _ in range(K):
    _input = list(map(int, input().split()))
    N = _input[0]
    watches_times = [(0, 0)]*N
    j = 0
    for i in range(1, 2*N, 2):
        watches_times[j] = (_input[i], _input[i + 1])
        j += 1
    print(can_be_one_removed(watches_times))