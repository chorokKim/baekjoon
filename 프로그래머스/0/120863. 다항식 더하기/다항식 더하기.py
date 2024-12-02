def solution(polynomial):
    answer = []
    vals = polynomial.split(" + ")
    x = 0
    c = 0
    for v in vals:
        if "x" in v:
            if v == "x":
                x += 1
            else:
                x += int(v[:-1])
        else:
            c += int(v)
    if x > 1:
        answer.append(str(x) + 'x')
    elif x == 1:
        answer.append('x')
    if c != 0:
        answer.append(str(c))
    if x == 0 and c == 0:
        answer.append('0')

    return ' + '.join(answer)