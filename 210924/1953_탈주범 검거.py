import sys
sys.stdin = open('1953_탈주범 검거.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 상하좌우와 연결된 다음 파이프의 인덱스
    np = [1, 0, 3, 2]

    # 연결 된 방향을 1로 표시한 파이프
    pipe = [[0, 0, 0, 0],
            [1, 1, 1, 1],   # 상하좌우
            [1, 1, 0, 0],   # 상하
            [0, 0, 1, 1],   # 좌우
            [1, 0, 0, 1],   # 상우
            [0, 1, 0, 1],   # 하우
            [0, 1, 1, 0],   # 하좌
            [1, 0, 1, 0]    # 상좌
            ]

    # 방문표시
    visited = [[0] * M for _ in range(N)]

    # 맨홀 뚜겅의 위치를 큐에 삽입 & 해당 좌표 방문표시
    Q = [(R, C)]
    visited[R][C] = 1
    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1
        # 해당 좌표까지 거리가 이미 L 이라면 더 탐색하지 않고 다음 좌표 탐색
        if visited[r][c] == L:
            continue

        # 4 방향에 대해 탐색
        for i in range(4):
            # 가고자 하는 방향에 파이프 방향이 없다면
            if pipe[tunnel[r][c]][i] == 0:
                continue

            nr = r + dr[i]
            nc = c + dc[i]

            # 가고자 하는 곳이 범위 밖에 있다면
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 가고자 하는 곳이 이미 방문했거나 그곳의 파이프와 연결되있지 않다면
            if visited[nr][nc] or pipe[tunnel[nr][nc]][np[i]] == 0:
                continue

            # 가고자 하는 곳에 경로표시
            visited[nr][nc] = visited[r][c] + 1
            # 큐에 삽입
            Q.append((nr, nc))

    print(f'#{tc} {ans}')