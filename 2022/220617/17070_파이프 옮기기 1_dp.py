n = int(input())
home = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

# 그래프 정보 입력
for i in range(n):
    home[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for i in range(2, n):
    if home[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 현재위치가 대각선인 경우 모든 경우가 가능하다.
        if home[r][c] == 0 and home[r][c - 1] == 0 and home[r - 1][c] == 0:
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if home[r][c] == 0:
            # 현재 위치가 가로인 경우 이전에 세로로 이동했거나 대각선으로 이동했어야 한다.
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            # 현재 위치가 세로인 경우 이전에 가로로 이동했거나 대각선으로 이동했어야 한다.
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))