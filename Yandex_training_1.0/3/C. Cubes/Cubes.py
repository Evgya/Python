N, M = map(int, input().split())
boris_cubes = set((int(input()) for _ in range(N)))
anna_cubes = set((int(input()) for _ in range(M)))

anna_and_boris_cubes = boris_cubes & anna_cubes
print(len(anna_and_boris_cubes))
print(" ".join(map(str, sorted(anna_and_boris_cubes))))

only_boris_cubes = boris_cubes - anna_and_boris_cubes
print(len(only_boris_cubes))
print(" ".join(map(str, sorted(only_boris_cubes))))

only_anna_cubes = anna_cubes - anna_and_boris_cubes
print(len(only_anna_cubes))
print(" ".join(map(str, sorted(only_anna_cubes))))
