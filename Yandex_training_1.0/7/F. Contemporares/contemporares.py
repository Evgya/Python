def get_sets_of_contemporares(times_of_life):
    events = []
    i = 0
    BEGIN, END = 1, -1
    for time_of_life in times_of_life:
        i += 1
        date_of_birth = time_of_life[0: 3][::-1]
        date_of_death = time_of_life[3: 6][::-1]
        date_of_eighteenth = date_of_birth[::1]
        date_of_eighteenth[0] += 18
        date_of_eightieth = date_of_birth[::1]
        date_of_eightieth[0] += 80
        if date_of_death > date_of_eighteenth:
            events.append((date_of_eighteenth, BEGIN, i))
            events.append((min(date_of_death, date_of_eightieth), END, i))
    if len(events) == 0:
        return [[0]]

    events.sort()
    contemporares = set()
    sets_of_contemporares = []
    for event in events:
        if event[1] == BEGIN:
            contemporares.add(event[2])
            prev_type = BEGIN
        else:
            if prev_type == BEGIN:
                sets_of_contemporares.append(contemporares.copy())
            prev_type = END
            contemporares.remove(event[2])
    return sets_of_contemporares

N = int(input())
times_of_life = tuple((list(map(int, input().split())) for _ in range(N)))
sets_of_contemporares = get_sets_of_contemporares(times_of_life)
for contemporares in sets_of_contemporares:
    print(*contemporares)
