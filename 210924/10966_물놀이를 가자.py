import sys
sys.stdin = open('10996_물놀이를 가자.txt', 'r')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    # 방문여부 & 거리체크
    dist = [[987654321] * M for _ in range(N)]

    # 적당한 크기의 큐 생성
    Q = [0] * (N * M)
    front = -1
    rear = -1

    # 물이 있는 곳을 일단 큐에 삽입
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                dist[i][j] = 0

    # front와 rear가 만날때까지 반복
    while front != rear:
        # 큐의 앞에서 부터 값을 선출
        front += 1
        r, c = Q[front]

        # 4방향에 대해 조사
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 가려고 하는 방향이 범위를 벗어난다면 제외
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 가려고 하는 방향이 땅이고, 방문한적이 없다면
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:
                # 해당 땅에 방문표시 & 거리표시(이전 땅까지의 거리 + 1)
                dist[nr][nc] = dist[r][c] + 1
                # 방문한 땅을 큐에 삽입
                rear += 1
                Q[rear] = (nr, nc)

    # 모든 땅에 대해 거리를 합산
    ans = 0
    for i in dist:
        for j in i:
            ans += j

    print(f'#{tc} {ans}')