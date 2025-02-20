from sys import stdin


def count_lans(length, lans):
    cnt = 0
    for l in lans:
        cnt += l // length
    return cnt

K, N = map(int, stdin.readline().split())
lans = [int(stdin.readline()) for _ in range(K)]

start = 1
end = 2**31 - 1
while start < end:
    mid = (start + end + 1) // 2
    cnt = count_lans(mid, lans)
    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid
print(start)