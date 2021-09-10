import sys

sys.stdin = open('2001_파리 퇴치.txt', 'r')

def fly(r, c, M):
    total = 0
    for i in range(M):
        for j in range(M):
            total += arr[r + i][c + j]
    return total

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    max_sum = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            result = fly(r, c, M)
            if result > max_sum:
                max_sum = result

    print(f'#{tc} {max_sum}')