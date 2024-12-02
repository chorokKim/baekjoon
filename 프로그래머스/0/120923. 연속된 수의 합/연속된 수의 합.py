def solution(num, total):
    c = 0
    for n in range(num):
        c += n
    x = (total - c) / num
    return [x + e for e in range(num)]