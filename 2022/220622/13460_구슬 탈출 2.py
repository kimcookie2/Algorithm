import sys
sys.stdin = open('input.txt', 'r')

def ball_move(dir):
    global Rr, Rc, Br, Bc
    Rnr, Rnc, Bnr, Bnc = 0, 0, 0, 0

    # 상
    if dir == 0:
        for i in range(Rr - 1, -1, -1):
            if board[i][Rc] == 'O':
                Rnr = i
                break
            if board[i][Rc] == '#':
                Rnr = i + 1
                break
        for j in range(Br - 1, -1, -1):
            if board[j][Bc] == 'O':
                Bnr = j
                break
            if board[j][Bc] == '#':
                Bnr = j + 1
                break
        if Rnr == Bnr and Rc == Bc and board[Rnr][Rc] != 'O':
            if Rr > Br:
                Rnr += 1
            elif Br > Rr:
                Bnr += 1
        Rr = Rnr
        Br = Bnr
    # 하
    if dir == 1:
        for i in range(Rr + 1, N):
            if board[i][Rc] == 'O':
                Rnr = i
                break
            if board[i][Rc] == '#':
                Rnr = i - 1
                break
        for j in range(Br + 1, N):
            if board[j][Bc] == 'O':
                Bnr = j
                break
            if board[j][Bc] == '#':
                Bnr = j - 1
                break
        if Rnr == Bnr and Rc == Bc and board[Rnr][Rc] != 'O':
            if Rr > Br:
                Bnr -= 1
            elif Br > Rr:
                Rnr -= 1
        Rr = Rnr
        Br = Bnr
    #좌
    if dir == 2:
        for i in range(Rc - 1, -1, -1):
            if board[Rr][i] == 'O':
                Rnc = i
                break
            if board[Rr][i] == '#':
                Rnc = i + 1
                break
        for j in range(Bc - 1, -1, -1):
            if board[Br][j] == 'O':
                Bnc = j
                break
            if board[Br][j] == '#':
                Bnc = j + 1
                break
        if Rnc == Bnc and Rr == Br and board[Rr][Rnc] != 'O':
            if Rc > Bc:
                Rnc += 1
            elif Bc > Rc:
                Bnc += 1
        Rc = Rnc
        Bc = Bnc
    #우
    if dir == 3:
        for i in range(Rc + 1, M):
            if board[Rr][i] == 'O':
                Rnc = i
                break
            if board[Rr][i] == '#':
                Rnc = i - 1
                break
        for j in range(Bc + 1, M):
            if board[Br][j] == 'O':
                Bnc = j
                break
            if board[Br][j] == '#':
                Bnc = j - 1
                break
        if Rnc == Bnc and Rr == Br and board[Rr][Rnc] != 'O':
            if Rc > Bc:
                Bnc -= 1
            elif Bc > Rc:
                Rnc -= 1
        Rc = Rnc
        Bc = Bnc

def move(n):
    global Rr, Rc, Br, Bc, result

    if Or == Br and Oc == Bc:
        return

    if Or == Rr and Oc == Rc:
        if Or == Br and Oc == Bc:
            return
        else:
            if n - 1 < result:
                result = n - 1
        return

    if n == 11:
        return

    for i in range(4):
        tmp_Rr, tmp_Rc = Rr, Rc
        tmp_Br, tmp_Bc = Br, Bc
        ball_move(i)
        if tmp_Rr == Rr and tmp_Rc == Rc and tmp_Br == Br and tmp_Bc == Bc:
            continue
        move(n + 1)
        Rr, Rc = tmp_Rr, tmp_Rc
        Br, Bc = tmp_Br, tmp_Bc

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(M):
        board[i][j] = tmp[j]
Rr, Rc = 0, 0
Br, Bc = 0, 0
Or, Oc = 0, 0
result = 11

for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            Br = r
            Bc = c
        if board[r][c] == 'R':
            Rr = r
            Rc = c
        if board[r][c] == 'O':
            Or = r
            Oc = c

board[Br][Bc] = '.'
board[Rr][Rc] = '.'

move(1)

if result == 11:
    print(-1)
else:
    print(result)

