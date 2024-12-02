def solution(polynomial):
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
    if x == 0:
         return str(c)
    elif x == 1:
        return 'x' if c == 0 else 'x + ' + str(c)
    else:
        return str(x) + 'x' if c == 0 else str(x) + 'x + ' + str(c)