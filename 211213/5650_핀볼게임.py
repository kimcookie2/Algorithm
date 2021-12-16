import sys
sys.stdin = open('5650_핀볼게임.txt', 'r')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

block = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2]
}

def check(r, c, dir):
    global result, ans

    while True:
        r = r + dr[dir]
        c = c + dc[dir]

        if r == -1 or r == N or c == -1 or c == N:
            dir = block[5][dir]
            result += 1
            continue

        if (r, c) == (sr, sc) or arr[r][c] == -1:
            if ans < result:
                ans = result
            break

        if 1 <= arr[r][c] <= 5:
            dir = block[arr[r][c]][dir]
            result += 1
            continue

        if arr[r][c] >= 6:
            r, c = wormhole_set[(r, c)]
            continue

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    wormhole = dict()
    wormhole_set = dict()
    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 6:
                if arr[i][j] in wormhole:
                    wormhole_set[wormhole[arr[i][j]]] = (i, j)
                    wormhole_set[(i, j)] = wormhole[arr[i][j]]
                else:
                    wormhole[arr[i][j]] = (i, j)

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                sr, sc = r, c
                for i in range(4):
                    result = 0
                    check(r, c, i)

    print(f'#{tc} {ans}')