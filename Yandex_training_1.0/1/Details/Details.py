def get_n_details(N, K, M ):
    n_details = 0
    if any((K < M, N < K)):
        return n_details
    while N >= K:
        n_K = N//K
        N = N%K
        n_details += n_K*(K//M)
        N += n_K*(K%M)
    return n_details
N, K, M = map(int, input().split())
print(get_n_details(N, K, M))
