def solution(num, k):
    answer = 0
    for n in str(num):
        answer += 1
        if int(n) == k:
            return answer
    return -1