import sys
sys.stdin = open("input1.txt", 'r')

dr = [0, 1, 1]
dc = [1, 0, 1]

def move(state, r, c):
    global result
    if r == N - 1 and c == N - 1:
        result += 1

    if r == N - 1 and state == 1:
        return
    if c == N - 1 and state == 0:
        return

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= N or nc >= N or home[nr][nc] == 1:
            continue
        if state == 0 and i == 1:
            continue
        if state == 1 and i == 0:
            continue
        if i == 2:
            if home[nr - 1][nc] == 1 or home[nr][nc - 1] == 1:
                continue

        move(i, nr, nc)

N = int(sys.stdin.readline())
home = [0] * N
for i in range(N):
    home[i] = list(map(int, sys.stdin.readline().split()))
result = 0

move(0, 0, 1)
print(result)