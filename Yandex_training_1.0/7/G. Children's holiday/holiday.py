def calc_min_time_and_distribution(work_times, relax_times, n_balls, M, N):
    participants = [0]*N
    if M == 0:
        return 0, participants
    periods = list(
        (work_times[i]*n_balls[i] + relax_times[i] for i in range(N))
    )
    max_period = max(periods)
    count_periods = list(map(lambda x: max_period//x + 1, periods))
    n_balls_in_periods = sum(
        map(lambda i: count_periods[i]*n_balls[i], range(N))
    )
    n_periods = M // n_balls_in_periods + 1
    count_periods = tuple(map(lambda x: x*n_periods, count_periods))
    events = []
    for i in range(N):
        for j in range(count_periods[i]):
            for k in range(1, n_balls[i] + 1):
                events.append((work_times[i]*k + j*periods[i], i))
    events.sort()
    participants = [0]*N
    total_balls = 0
    for event in events:
        participants[event[1]] += 1
        total_balls += 1
        if total_balls == M:
            return event[0], participants

M, N = map(int, input().split())
work_times = [0]*N
relax_times = [0]*N
n_balls = [0]*N
for i in range(N):
    T, Z, Y = map(int, input().split())
    work_times[i] = T
    relax_times[i] = Y
    n_balls[i] = Z
total_time, participants = calc_min_time_and_distribution(
    work_times, relax_times, n_balls, M, N
)
print(total_time)
print(*participants)
