def count_unwatched_students(watch_segments, N, M):
    events = [0]*2*M
    WATCH_START, WATCH_END = -1, 1
    j = 0
    for i in range(0, 2*M - 1, 2):
        events[i] = (watch_segments[j][0], WATCH_START)
        events[i + 1] = (watch_segments[j][1], WATCH_END)
        j += 1
    events.sort()

    watchers = 0
    watched_students = 0
    for i in range(len(events)):
        if watchers > 0:
            watched_students += events[i][0] - events[i - 1][0]
        else:
            watched_students += 1

        if events[i][1] == WATCH_START:
            watchers += 1
        else:
            watchers -= 1

    return N - watched_students


N, M = map(int, input().split())
watch_segments = tuple((tuple(map(int, input().split())) for _ in range(M)))
print(count_unwatched_students(watch_segments, N, M))
