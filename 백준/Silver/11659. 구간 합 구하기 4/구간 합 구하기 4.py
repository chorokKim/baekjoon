from sys import stdin

N, M = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
d = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    d[i] = d[i - 1] + numbers[i - 1]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(d[j] - d[i - 1])