from sys import stdin

N = int(stdin.readline())

def draw_star(n):
    if n%2 == 1:
        return["  *   ", " * *  ", "***** "]
    
    stars = draw_star(n // 2)
    row = []
    for s in stars:
        row.append(' '*(n//2) + s + ' '*(n//2))
    for s in stars:
        row.append(s*2)
    return row

answer = draw_star(N)
print("\n".join(answer))