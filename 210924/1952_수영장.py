import sys
sys.stdin = open('1952_수영장.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    d, m1, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(m1, plan[1] * d)
    dp[2] = dp[1] + min(m1, plan[2] * d)
    for i in range(3, 13):
        dp[i] = min(dp[i - 3] + m3, # 3달 이용권
                    dp[i - 1] + m1, # 1달 이용권
                    dp[i - 1] + plan[i] * d # 1일 이용권
                    )

    # 1년 이용권과 비교
    min_cost = min(dp[12], y)

    print(f'#{tc} {min_cost}')