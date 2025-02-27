def slope(dot1, dot2):
    return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])

def solution(dots):
    if slope(dots[0], dots[1]) == slope(dots[2], dots[3]):
        return 1
    if slope(dots[0], dots[2]) == slope(dots[1], dots[3]):
        return 1
    if slope(dots[0], dots[3]) == slope(dots[1], dots[2]):
        return 1
    else:
        return 0