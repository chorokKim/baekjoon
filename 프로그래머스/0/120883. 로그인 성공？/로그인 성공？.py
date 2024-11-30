def solution(id_pw, db):
    answer = 'fail'
    for id, pw in db:
        if id_pw[0] == id:
            return "login" if id_pw[1] == pw else "wrong pw"
    return answer