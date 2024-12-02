def solution(board):
    B = len(board)
    answer = 0
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    mine = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                mine.append([i, j])
    for x, y in mine:
        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < B and 0 <= my < B:
                board[mx][my] = 1
    for x in range(B):
        for y in range(B):
            if board[x][y] == 0:
                answer += 1
    return answer