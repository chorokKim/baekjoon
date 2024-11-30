def solution(n):
    answer = 0
    i = 0
    while i != n:
        i += 1
        answer += 1
        while "3" in str(answer) or answer % 3 == 0:
            answer += 1
    return answer