import sys
sys.stdin = open('14501_퇴사.txt', 'r')

N = int(input())
Time = [0] * (N)
Pay = [0] * (N)
for i in range(N):
    Time[i], Pay[i] = map(int, input().split())

# d는 현재 날짜, reward는 현재까지 수익
def work(d, reward):
    global ans

    # d가 N보다 커진다면 return
    if d > N:
        return

    # d가 N이 되었을 때,
    if d == N:
        # 현재까지 reward가 더 크다면 저장
        if ans < reward:
            ans = reward
        return

    # 현재 일에서 상담시작, 수익추가
    work(d + Time[d], reward + Pay[d])
    # 다음 일자로 넘어가기
    work(d + 1, reward)

ans = 0
work(0, 0)

print(ans)