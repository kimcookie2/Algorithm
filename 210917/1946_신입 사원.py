import sys
sys.stdin = open('1946_신입 사원.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = [0] * N
    for i in range(N):
        scores[i] = list(map(int, input().split()))
    scores = sorted(scores)
    cnt = 1
    second_min = scores[0][1]

    for i in range(1, N):
        if scores[i][1] < second_min:
            second_min = scores[i][1]
            cnt += 1
            if second_min == 1:
                break

    print(cnt)
