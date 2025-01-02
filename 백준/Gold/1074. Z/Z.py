from sys import stdin

N, r, c = map(int, stdin.readline().split())

def travel(N, r, c):
    if N == 0:
        return 0
    half = 2 ** (N - 1)
    if r < half and c < half: # 1
        return travel(N - 1, r, c)
    elif r < half and c >= half: # 2
        return half * half + travel(N - 1, r, c - half)
    elif r >= half and c < half: # 3
        return 2 * half * half + travel(N - 1, r - half, c)
    return 3 * half * half + travel(N - 1, r - half, c - half)

print(travel(N, r, c))