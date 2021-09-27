import sys
sys.stdin = open('1949_등산로 조성.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 해당 좌표에서 가장 긴 등산로를 찾는 함수
def search(r, c, road, work):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    # 4방향에 대해 조사
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 가려고 하는 방향이 범위 내에 있고, 방문하지 않았다면
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            # 가려고 하는 방향이 더 낮다면
            if mountain[nr][nc] < mountain[r][c]:
                search(nr, nc, road + 1, work)
            # 더 높거나 같은 방향으로 이동한다면 & 그 방향이 공사가 가능하다면
            elif work and mountain[nr][nc] - K < mountain[r][c]:
                # 이번 탐색에서만 공사할것이기 때문에 기록
                tmp = mountain[nr][nc]
                # 현재 위치보다 높이를 1 작게 공사
                mountain[nr][nc] = mountain[r][c] - 1
                # 공사 진행
                search(nr, nc, road + 1, 0)
                # 다음 탐색을 위해 원상복구
                mountain[nr][nc] = tmp

    # 다음 경로 탐색을 위해 복구
    visited[r][c] = 0

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    # 가장 높은 봉우리의 높이 찾기
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_h:
                max_h = mountain[i][j]

    # 방문여부 체크
    visited = [[0] * N for _ in range(N)]
    ans = 0

    # 가장 높은 봉우리라면 경로탐색 시작
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                search(i, j, 1, 1)

    print(f'#{tc} {ans}')