def solution(emergency):
    answer = [sorted(emergency, reverse=True).index(i) + 1 for i in emergency]
    return answer