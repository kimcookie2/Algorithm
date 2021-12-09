import sys
sys.stdin = open('2383_점심 식사시간.txt', 'r')

def down_stairs(entrance, arrival_times):
    if not arrival_times:
        return 0

    arrival_times.sort()
    people_in_stair_by_time = [0] * 200

    k = Spos[entrance][2]
    for t in arrival_times:
        tt = t + 1
        while people_in_stair_by_time[tt] >= 3:
            tt += 1
        for j in range(tt, tt + k):
            people_in_stair_by_time[j] += 1

    for i in range(199, 0, -1):
        if people_in_stair_by_time[i]:
            return i + 1

def move(entrance_choices, ppos_cnt):
    arrival0 = []
    arrival1 = []

    for i in range(ppos_cnt):
        if entrance_choices & (1 << i) == 0:
            arrival0.append(dist[i][0])
        else:
            arrival1.append(dist[i][1])

    return max(down_stairs(0, arrival0), down_stairs(1, arrival1))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    Ppos = []
    Spos = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                Ppos.append([i, j])
            elif m[i][j] != 0 :
                Spos.append([i, j, m[i][j]])

    dist = [[0] * 2 for i in range(len(Ppos))]
    for i in range(len(Ppos)):
        dist[i][0] = abs(Ppos[i][0] - Spos[0][0]) + abs(Ppos[i][1] - Spos[0][1])
        dist[i][1] = abs(Ppos[i][0] - Spos[1][0]) + abs(Ppos[i][1] - Spos[1][1])

    ans = 10e9
    for entrance_choices in range(1 << len(Ppos)):
        ans = min(ans, move(entrance_choices, len(Ppos)))

    print(f'#{tc} {ans}')