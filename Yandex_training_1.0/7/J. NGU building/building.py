def find_min_overlap(blocks, W, L):
    total_area = W*L
    areas = [0]*(len(blocks) + 1)
    events = [0]*(2*len(blocks))
    k, j = 0, 1
    BEGIN, END = 1, -1
    for i in range(0, len(events) - 1, 2):
        areas[j] = (
            abs(blocks[k][0] - blocks[k][3])*abs(blocks[k][1] - blocks[k][4])
        )
        events[i] = (min(blocks[k][2], blocks[k][5]), BEGIN, j)
        events[i + 1] = (max(blocks[k][2], blocks[k][5]), END, j)
        j += 1
        k += 1
    events.sort()
    cur_used = 0
    min_used = len(blocks) + 1
    cur_area = 0
    for event in events:
        if event[1] == BEGIN:
            cur_area += areas[event[2]]
            cur_used += 1
            if cur_area == total_area and cur_used < min_used:
                min_used = cur_used
        else:
            cur_used -= 1
            cur_area -= areas[event[2]]
    blocks_used = set()
    if min_used == len(blocks) + 1:
        return blocks_used
    cur_area = 0
    for event in events:
        if event[1] == BEGIN:
            cur_area += areas[event[2]]
            blocks_used.add(event[2])
            if cur_area == total_area and len(blocks_used) == min_used:
                return blocks_used
        else:
            blocks_used.remove(event[2])
            cur_area -= areas[event[2]]

N, W, L = map(int, input().split())
blocks = tuple((tuple(map(int, input().split())) for _ in range(N)))
blocks_used = find_min_overlap(blocks, W, L)
if len(blocks_used) == 0:
    print("NO")
else:
    print("YES")
    print(len(blocks_used))
    print(*blocks_used)
