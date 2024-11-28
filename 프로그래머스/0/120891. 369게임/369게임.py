def solution(order):
    answer = 0
    for n in str(order):
        if n in "369":
            answer += 1
    return answer