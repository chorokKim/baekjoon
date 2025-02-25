from sys import stdin

N, M = map(int, stdin.readline().split())
accounts = {}
for _ in range(N):
    site, pw = stdin.readline().split()
    accounts[site] = pw

for _ in range(M):
    print(accounts[stdin.readline().strip()])