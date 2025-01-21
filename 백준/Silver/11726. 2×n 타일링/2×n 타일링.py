from sys import stdin

n = int(stdin.readline())
d = [0 for _ in range(n + 1)]

if n < 3:
    print(n)
else:
    d[1], d[2] = 1, 2
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 10007
    print(d[n])