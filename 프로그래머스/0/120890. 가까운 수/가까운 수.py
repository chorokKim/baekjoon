def solution(array, n):
    array.sort()
    val = [abs(n - a) for a in array]
    return array[val.index(min(val))]