N, K = [int(i) for i in input().split(" ")]
count = [0 for _ in range(12)]
result = 0

for _ in range(N):
    S, Y = input().split(" ")
    count[int(S)*6 + int(Y) - 1] += 1

for cnt in count:
    result += cnt//K
    if cnt%K > 0:
        result += cnt%K

print(result)