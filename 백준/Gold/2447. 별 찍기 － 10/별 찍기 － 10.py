from sys import stdin

N = int(stdin.readline())

def draw_star(n):
    if n == 1:
        return["*"]
    
    stars = draw_star(n // 3)
    row = []
    for s in stars:
        row.append(s*3)
    for s in stars:
        row.append(s + ' '*(n//3) + s)
    for s in stars:
        row.append(s*3)
    return row

answer = draw_star(N)
print("\n".join(answer))