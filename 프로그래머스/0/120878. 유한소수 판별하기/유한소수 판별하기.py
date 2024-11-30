def solution(a, b):
    for i in range(max(a, b), 0 , -1):
        if a % i == 0 and b % i == 0:
            b //= i
            break
    num = []
    i = 2
    while i <= b:
        if b % i == 0:
            b //= i
            num.append(i)
        else:
            i += 1
    return 1 if all([i in [2, 5] for i in num]) else 2