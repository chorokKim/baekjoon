def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        X, cal, Y, Z = int(q[0]), q[1], int(q[2]), int(q[4])

        if cal == "+":
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if X - Y == Z:
                answer.append("O")
            else:
                answer.append("X")
    return answer