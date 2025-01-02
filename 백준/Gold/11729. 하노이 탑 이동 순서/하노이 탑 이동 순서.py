from sys import stdin

N = int(stdin.readline())

def hanoi(a, b, N):
    if N == 1:
        print(a, b)
        return
    hanoi(a, 6 - a - b, N - 1)
    print(a, b)
    hanoi(6 - a - b, b, N - 1)

print(2**N - 1)
hanoi(1, 3, N)