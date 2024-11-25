def solution(balls, share):
    answer = 1
    for i in range(balls, share, -1):
        answer *= i
    for i in range(balls - share, 0, -1):
        answer /= i
    return answer