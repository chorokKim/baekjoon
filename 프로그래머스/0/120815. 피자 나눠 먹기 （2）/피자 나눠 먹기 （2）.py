def solution(n):
    answer = 0
    for i in range(6, 0, -1):
        if n%i == 0 and 6%i == 0:
            answer = n/i
            break
    return answer