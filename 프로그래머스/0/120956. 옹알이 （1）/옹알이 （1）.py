def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for w in words:
            b = b.replace(w, " ")
        if b.strip() == "":
            answer += 1
            continue
    return answer