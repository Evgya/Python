def find_permutation_to_fix(bodies, N):
    permutation = []
    for i in range(1, N - 1):
        if (bodies[i] != i):
            cur = i
            while(bodies[cur] != i):
                permutation.append((cur, N - 1))
                bodies[cur], bodies[N - 1] = bodies[N - 1], bodies[cur]
                cur = bodies[N - 1]
            permutation.append((cur, N))
            bodies[cur], bodies[N] = bodies[N], bodies[cur]
            permutation.append((i, N))
            bodies[i], bodies[N] = bodies[N], bodies[i]
            permutation.append((cur, N-1))
            bodies[N - 1], bodies[cur] = bodies[cur], bodies[N - 1]

    if bodies[N - 1] == N:
        permutation.append((N - 1, N))
        bodies[N], bodies[N - 1] = bodies[N - 1], bodies[N]
    return permutation

N, M = map(int, input().split())
bodies = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    bodies[a], bodies[b] = bodies[b], bodies[a]
for transpos in find_permutation_to_fix(bodies, N):
    print(transpos[0], transpos[1])
