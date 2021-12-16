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

    # 모든 미생물들이 이동
    for micro_idx in range(K):
        micro = micros[micro_idx]
        # r, c, 미생물의 수, 이동방향
        r, c, tmp, dir = micro

        # 미생물의 수가 0이라면 다음 미생물 조사
        if tmp == 0:
            continue

        # 이동방향에 따른 미생물의 다음 위치
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 미생물의 다음 위치가 약품 위라면,
        if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
            # 미생물의 수가 절반으로 감소 / 방향 전환
            micro[2] = micro[2] // 2
            micro[3] = reverse[micro[3]]

        # 미생물 합체
        # 이미 다음 위치에 도착한 미생물이 없다면,
        if (nr, nc) not in check:
            # check 표시(nr, nc 기준)
            # 전체 미생물의 수, 현재 까지의 미생물 최대 값, 방향, 이 위치에서 최대값을 가진 미생물의 index
            check[(nr, nc)] = (tmp, tmp, dir, micro_idx)
        # 이미 다음 위치에 도착한 미생물이 있다면,
        else:
            # 새로 도달한 미생물의 양이 더 많다면
            if check[(nr, nc)][1] < tmp:
                # 최대값 갱신 / 이 위치에서 최대값을 가진 미생물 갱신
                new_total = check[(nr, nc)][0] + tmp
                new_max = tmp
                new_dir = dir
                pre_idx = check[(nr, nc)][3]
                check[(nr, nc)] = (new_total, new_max, new_dir, micro_idx)
                micro[2] = new_total
                micro[3] = new_dir
                # 합쳐진 미생물은 0으로 초기화
                micros[pre_idx][2] = 0
            # 기존에 있던 미생물의 양이 더 많다면
            else:
                # 최대값 갱신
                new_total = check[(nr, nc)][0] + tmp
                pre_idx = check[(nr, nc)][3]
                check[(nr, nc)] = (new_total, check[(nr, nc)][1], check[(nr, nc)][2], pre_idx)
                micro[2] = 0
                # 합쳐진 미생물은 0으로 초기화
                micros[pre_idx][2] = new_total

        # 미생물 이동
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