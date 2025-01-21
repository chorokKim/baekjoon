from sys import stdin

N = int(stdin.readline())
costs = [[0, 0, 0]]
d = [[0, 0, 0]]
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    costs.append(row)
    d.append([0, 0, 0])

d[1] = costs[1]

for i in range(2, N + 1):
    d[i][0] = costs[i][0] + min(d[i - 1][1:])
    d[i][1] = costs[i][1] + min(d[i - 1][::2])
    d[i][2] = costs[i][2] + min(d[i - 1][:-1])

print(min(d[N]))