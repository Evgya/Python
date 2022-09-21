from collections import deque


def get_variants_arrangement(X, D):
    SEGMENT_START, SEGMENT_END = -1, 1
    events = [(0, 0)]*(2*len(X))
    qeque = deque()
    j = 0
    for i in range(0, 2*N - 1, 2):
        events[i] = (X[j], SEGMENT_START)
        events[i + 1] = (X[j] + D, SEGMENT_END)
        j += 1
    events.sort()
    variants_used = 0
    variants = {x: 0 for x in X}

    for event in events:
        if event[1] == SEGMENT_START:
            variants_used += 1
            if len(qeque) == 0:
                variants[event[0]] = variants_used
            else:
                variants[event[0]] = qeque.popleft()
        else:
            variants_used -= 1
            qeque.append(variants[event[0] - D])
    return variants


N, D = map(int, input().split())
X = tuple(map(int, input().split()))
variants_arrangement = get_variants_arrangement(X, D)
print(max(variants_arrangement.values()))
print(" ".join((str(variants_arrangement[x]) for x in X)))
