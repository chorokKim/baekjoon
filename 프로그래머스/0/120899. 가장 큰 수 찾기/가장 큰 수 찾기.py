def solution(array):
    max_num = max(array)
    answer = [max_num, array.index(max_num)]
    return answer