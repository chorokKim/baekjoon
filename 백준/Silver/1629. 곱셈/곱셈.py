from sys import stdin

A, B, C = map(int, stdin.readline().split())

def expo(A, B, C):
    if B == 1:
        return A % C
    val = expo(A, B//2, C)
    val = val * val % C
    if B % 2 == 0:
        return val
    return val * A % C

print(expo(A, B, C))