from sys import stdin

n, m = map(int, stdin.readline().split())

def recursive(k, w):
    p = []
    if k == 2:
        if w == 0: # 3
            p = [1, 1]
        elif w == 1: # 2
            p = [1, 2]
        elif w == 2: # 1
            p = [2, 2]
        elif w == 3: # 4
            p = [2, 1]
        return p
    
    half = k // 2
    quarter = w // (half*half)

    if quarter == 0: # 3
        p = recursive(half, w%(half*half))
        p = [p[1], p[0]]
    elif quarter == 1: # 2
        p = recursive(half, w%(half*half))
        p[1] += half
    elif quarter == 2: # 1
        p = recursive(half, w%(half*half))
        p[0] += half
        p[1] += half
    elif quarter == 3: # 4
        p = recursive(half, w%(half*half))
        p = [2*half - p[1] + 1, half - p[0] + 1]
    return p

print(*recursive(n, m - 1))