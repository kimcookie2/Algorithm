import sys
sys.stdin = open('2105_디저트 카페.txt', 'r')

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def cafe(r, c, n, d):
    global ans, sr, sc

    if d == 4:
        return

    nr = r + dr[d]
    nc = c + dc[d]

    if nr == sr and nc == sc and d == 3:
        if ans < n:
            ans = n
        return

    if nr < 0 or N <= nr or nc < 0 or N <= nc:
        return

    if visited[nr][nc] == 0 and tried[desserts[nr][nc]] == 0:
        visited[nr][nc] = 1
        tried[desserts[nr][nc]] = 1

        cafe(nr, nc, n + 1, d)
        cafe(nr, nc, n + 1, d + 1)

        visited[nr][nc] = 0
        tried[desserts[nr][nc]] = 0
    else:
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    desserts = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    tried = [0] * 101
    ans = 0

    for i in range(N):
        for j in range(N):
            sr, sc = i, j
            visited[i][j] = 1
            tried[desserts[i][j]] = 1
            cafe(i, j, 1, 0)
            visited[i][j] = 0
            tried[desserts[i][j]] = 0

    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} -1')