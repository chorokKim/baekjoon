from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)