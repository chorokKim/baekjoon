def solution(score):
    average = [sum(s) for s in score]
    sorted_average = sorted(average, reverse=True)
    return [sorted_average.index(a) + 1 for a in average]