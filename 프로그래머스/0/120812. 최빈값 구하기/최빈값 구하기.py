def solution(array):
    answer = 0
    count = [0 for _ in range(1000)]
    for a in array:
        count[a] += 1
    if count.count(max(count)) > 1:
        answer = -1
    else:
        answer = count.index(max(count))
    return answer