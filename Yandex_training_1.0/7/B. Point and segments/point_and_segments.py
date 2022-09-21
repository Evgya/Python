def count_segments_point_belong_to(segments, points):
    events = [0]*(2*len(segments) + len(points))
    SEGMENT_START, POINT, SEGMENT_END = -1, 0, 1
    j = 0
    for i in range(0, 2*len(segments) - 1, 2):
        begin = min(segments[j][0], segments[j][1])
        end = max(segments[j][0], segments[j][1])
        events[i] = (begin, SEGMENT_START)
        events[i + 1] = (end, SEGMENT_END)
        j += 1
    j = 0
    for i in range(2*len(segments), 2*len(segments) + len(points)):
        events[i] = (points[j], POINT)
        j += 1
    events.sort()
    counts_segments = {point: 0 for point in points}
    count_segments = 0
    for event in events:
        if event[1] == SEGMENT_START:
            count_segments += 1
        elif event[1] == POINT:
            counts_segments[event[0]] = str(count_segments)
        else:
            count_segments -= 1

    return " ".join((counts_segments[point] for point in points))

n, m = map(int, input().split())
segments = tuple((tuple(map(int, input().split())) for _ in range(n)))
points = tuple(map(int, input().split()))
print(count_segments_point_belong_to(segments, points))
