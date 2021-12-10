import sys
sys.stdin = open('2382_미생물 격리.txt', 'r')

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

reverse = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

def move():
    check = {}

    for micro_idx in range(K):
        micro = micros[micro_idx]
        r, c, tmp, dir = micro

        if tmp == 0:
            continue

        nr = r + dr[dir]
        nc = c + dc[dir]

        if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
            micro[2] = micro[2] // 2
            micro[3] = reverse[micro[3]]

        if (nr, nc) not in check:
            # total, now_max, direction, idx
            check[(nr, nc)] = (tmp, tmp, dir, micro_idx)
        else:
            if check[(nr, nc)][1] < tmp:
                new_total = check[(nr, nc)][0] + tmp
                new_max = tmp
                new_dir = dir
                pre_idx = check[(nr, nc)][3]

                check[(nr, nc)] = (new_total, new_max, new_dir, micro_idx)
                micro[2] = new_total
                micro[3] = new_dir
                micros[pre_idx][2] = 0

            else:
                new_total = check[(nr, nc)][0] + tmp
                pre_idx = check[(nr, nc)][3]
                check[(nr, nc)] = (new_total, check[(nr, nc)][1], check[(nr, nc)][2], pre_idx)
                micro[2] = 0
                micros[pre_idx][2] = new_total

        micro[0], micro[1] = nr, nc

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # micro = [r, c, 미생물 수, 이동방향]
    micros = [list(map(int, input().split())) for _ in range(K)]

    for i in range(M):
        move()

    ans = 0

    for micro in micros:
        ans += micro[2]

    print(f'#{tc} {ans}')