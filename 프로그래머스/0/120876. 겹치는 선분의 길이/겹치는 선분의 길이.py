def solution(lines):
    answer = 0
    count = [0 for _ in range(200)]
    for line in lines:
        for d in range(line[0], line[1]):
            count[d + 100] += 1
    for c in count:
        if c > 1:
            answer += 1
    return answer