def solution(common):
    answer = 0
    val = 0
    if common[2] - common[1] == common[1] - common[0]:
        val = common[1] - common[0]
        answer += common[-1] + val
    else:
        val = common[1] / common[0]
        answer = common[-1] * val
    return answer