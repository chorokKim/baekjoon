def solution(sides):
    max_side = max(sides)
    return 1 if max_side < sum(sides) - max_side else 2