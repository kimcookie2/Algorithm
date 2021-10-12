import sys
sys.stdin = open('5656_벽돌깨기.txt', 'r')

import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def throw(k):
    global arr, ans

    if k == N:

        cnt = 0
        for i in range(H):
            cnt += arr[i].count(0)
        result = W * H - cnt

        if ans > result:
            ans = result

        return

    for c in range(W):
        for r in range(H):
            if arr[r][c] != 0:
                tmp_list = copy.deepcopy(arr)
                boom(r, c)
                my_sort(arr)
                throw(k + 1)
                arr = tmp_list
                break
        else:
            throw(k + 1)

def boom(r, c):
    tmp = arr[r][c]
    arr[r][c] = 0

    if tmp > 1:
        for n in range(1, tmp):
            for dir in range(4):
                nr = r + dr[dir] * n
                nc = c + dc[dir] * n

                if 0 <= nr < H and 0 <= nc < W:
                    tmp2 = arr[nr][nc]
                    if tmp2 > 1:
                        boom(nr, nc)
                    arr[nr][nc] = 0


def my_sort(arr):
    for c in range(W):
        Q = []
        for r in range(H - 1, -1, -1):
            if arr[r][c]:
                Q.append(arr[r][c])
        for r in range(H - 1, -1, -1):
            if Q:
                arr[r][c] = Q.pop(0)
            else:
                arr[r][c] = 0

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 987654321

    throw(0)
    print(f'#{tc} {ans}')