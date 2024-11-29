def solution(n):
    arr = []
    i = 2
    while i <= n:
        if n % i == 0:
            n = n // i
            arr.append(i)
        else:
            i += 1
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
    return answer