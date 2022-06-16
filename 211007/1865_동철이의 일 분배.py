import sys
sys.stdin = open('동철이의 일 분배.txt', 'r')

def work(p, percent):
    global ans

    # ans 보다 계산된 percent 값이 적으면 return
    if ans >= percent:
        return

    # 마지막 사람까지 일을 끝냈다면,
    if p == N:
        # ans 보다 계산된 percent 값이 크다면 ans 갱신
        if ans < percent:
            ans = percent
        return

    # 모든 일에 대해
    for i in range(N):
        # i 번째 일을 아직 수행하지 않았다면,
        if visited[i] == 0:
            # i 번째 일 수행
            visited[i] = 1
            # 다음 사람이 일 수행(p + 1) / 현재 사람이 i 번째 일을 수행할 확률 누적
            work(p + 1, percent * arr[p][i])
            # 초기화
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 일을 성공할 확률을 미리 소수로 계산
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0

    work(0, 1)
    ans = ans * 100
    # 소수점 6번째까지 출력
    print(f'#{tc} {ans:0.6f}')