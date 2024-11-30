def solution(sides):
    answer = sum(sides) - max(sides) - 1
    for i in range(1, max(sides) + 1):
        if i + min(sides) > max(sides):
            answer += 1
    return answer