def solution(triangle):
    answer = 0
    n = len(triangle)

    dp = [0] * n
    for i in range(n):
        dp[i] = [0] * (i + 1)

    dp[0][0] = triangle[0][0]
    for r in range(1, n):
        for c in range(len(dp[r])):
            if c - 1 < 0:
                dp[r][c] = dp[r - 1][c] + triangle[r][c]
            elif c >= len(dp[r]) - 1:
                dp[r][c] = dp[r - 1][c - 1] + triangle[r][c]
            else:
                dp[r][c] = max(dp[r - 1][c - 1] + triangle[r][c], dp[r - 1][c] + triangle[r][c])

    return max(dp[n - 1])