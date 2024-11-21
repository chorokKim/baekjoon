def solution(rsp):
    answer = ''
    rsp_dict = {'2': '0', '0': '5', '5': '2'}
    for i in rsp:
        answer += rsp_dict[i]
    return answer