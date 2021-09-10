import sys
sys.stdin = open('11315_오목 판정.txt', 'r')

# 우, 하, 좌하, 우하
dr = [0, 1, 1, 1]
dc = [1, 0, -1, 1]

def check(r, c):
    sr = r
    sc = c
    for i in range(4):
        checking = [0] * 4
        r = sr
        c = sc
        for j in range(4):
            r += dr[i]
            c += dc[i]

            if 0 <= r < N and 0 <= c < N:
                checking[j] = data[r][c]

        if checking == ['o', 'o', 'o', 'o']:
            return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [0] * N
    for i in range(N):
        data[i] = input()
    cnt = 0

    for r in range(N):
        for c in range(N):
            if data[r][c] == 'o':
                if check(r, c):
                    cnt += 1

    if cnt >= 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')