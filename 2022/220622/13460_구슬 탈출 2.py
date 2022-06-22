import sys
sys.stdin = open('input.txt', 'r')

def ball_move(dir):
    global Rr, Rc, Br, Bc
    board[Rr][Rc] = '.'
    board[Br][Bc] = '.'

    # 상
    if dir == 0:
        for i in range(Rr - 1, -1, -1):
            if board[i][Rc] == '#':
                Rnr = i + 1
                break
        for j in range(Br - 1, -1, -1):
            if board[j][Bc] == '#':
                Bnr = j + 1
                break
        if Rnr == Bnr and Rc == Bc:
            if Rr > Br:
                Rnr += 1
            elif Br > Rr:
                Bnr += 1
        Rr = Rnr
        Br = Bnr
    # 하
    if dir == 1:
        for i in range(Rr + 1, N):
            if board[i][Rc] == '#':
                Rnr = i - 1
                break
        for j in range(Br + 1, N):
            if board[j][Bc] == '#':
                Bnr = j - 1
                break
        if Rnr == Bnr and Rc == Bc:
            if Rr > Br:
                Bnr -= 1
            elif Br > Rr:
                Rnr -= 1
        Rr = Rnr
        Br = Bnr
    #좌
    if dir == 2:
        for i in range(Rc - 1, -1, -1):
            if board[Rr][i] == '#':
                Rnc = i + 1
                break
        for j in range(Bc - 1, -1, -1):
            if board[Br][j] == '#':
                Bnc = j + 1
                break
        if Rnc == Bnc and Rr == Br:
            if Rc > Bc:
                Rnc += 1
            elif Bc > Rc:
                Bnc += 1
        Rc = Rnc
        Bc = Bnc
    #우
    if dir == 3:
        for i in range(Rc + 1, N):
            if board[Rr][i] == '#':
                Rnc = i - 1
                break
        for j in range(Bc + 1, N):
            if board[Br][j] == '#':
                Bnc = j - 1
                break
        if Rnc == Bnc and Rr == Br:
            if Rc > Bc:
                Bnc -= 1
            elif Bc > Rc:
                Rnc -= 1
        Rc = Rnc
        Bc = Bnc

    board[Rr][Rc] = 'R'
    board[Br][Bc] = 'B'

def move(n):
    for i in range(4):
        ball_move(i)


N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(M):
        board[i][j] = tmp[j]
Rr, Rc = 0, 0
Br, Bc = 0, 0

for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            Br = r
            Bc = c
        if board[r][c] == 'R':
            Rr = r
            Rc = c



for lst in board:
    print(*lst)

