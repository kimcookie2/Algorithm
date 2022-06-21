import sys
sys.stdin = open('input.txt', 'r')

# 오른쪽 비교 후 반영
def fish_diff_right(checked, diff, r, c):
    d = diff // 5
    if d > 0:
        checked[r][c] -= d
        checked[r + 1][c] += d
    elif d < 0:
        if diff % 5 != 0:
            d = -1 * d - 1
        else:
            d = -1 * d
        checked[r][c] += d
        checked[r + 1][c] -= d

def fish_diff_up(checked, diff, r, c):
    d = diff // 5
    if d > 0:
        checked[r][c] -= d
        checked[r][c + 1] += d
    elif d < 0:
        if diff % 5 != 0:
            d = -1 * d - 1
        else:
            d = -1 * d
        checked[r][c] += d
        checked[r][c + 1] -= d

def fish_move(n, fish):
    checked = [[0] * n for _ in range(n)]
    for r in range(n - 1):
        if fish[r]:
            # 길이가 1이라면 오른쪽 이랑만 비교
            if len(fish[r]) == 1:
                diff = fish[r][0] - fish[r + 1][0]
                fish_diff_right(checked, diff, r, 0)
            # 길이가 1보다 크고 다음것과 크기가 같다면 위쪽와 오른쪽을 비교
            elif len(fish[r]) > 1 and len(fish[r]) == len(fish[r + 1]):
                for c in range(len(fish[r]) - 1):
                    # 위쪽 비교
                    diff_up = fish[r][c] - fish[r][c + 1]
                    fish_diff_up(checked, diff_up, r, c)
                    # 오른쪽 비교
                    diff_right = fish[r][c] - fish[r + 1][c]
                    fish_diff_right(checked, diff_right, r, c)
                # 맨 위에서는 오른쪽 비교
                c = len(fish[r]) - 1
                diff_right = fish[r][c] - fish[r + 1][c]
                fish_diff_right(checked, diff_right, r, c)
            # 길이가 1보다 크고 다음것이 길이가 1이라면 맨 아래만 오른쪽 비교
            elif len(fish[r]) > 1 and len(fish[r + 1]) == 1:
                diff = fish[r][0] - fish[r + 1][0]
                fish_diff_right(checked, diff, r, 0)
                for c in range(len(fish[r]) - 1):
                    # 위쪽 비교
                    diff_up = fish[r][c] - fish[r][c + 1]
                    fish_diff_up(checked, diff_up, r, c)
    # 맨 끝 열인데, 길이가 1이 아니라면 위쪽 비교해줘야 함!!!
    r = len(fish) - 1
    if len(fish[r]) > 1:
        for c in range(len(fish[r]) - 1):
            # 위쪽 비교
            diff_up = fish[r][c] - fish[r][c + 1]
            fish_diff_up(checked, diff_up, r, c)

    return checked

def line():
    idx = 0
    for r in range(N):
        if len(fish[r]) > 1:
            for _ in range(len(fish[r])):
                fish[idx].append(fish[r].pop(0))
                idx += 1

N, K = map(int, input().split())
fish_input = list(map(int, input().split()))
fish = [[] for _ in range(N)]

for i in range(N):
    fish[i].append(fish_input[i])

result = 1
while 1:
    min_fish = 123456789
    for i in range(len(fish)):
        min_fish = min(fish[i][0], min_fish)
    for i in range(len(fish)):
        if min_fish == fish[i][0]:
            fish[i][0] += 1

    # 우선 가장 왼쪽에 있는 것을 오른쪽 어항 위에 쌓기
    fish[1].append(fish[0].pop(0))

    # 공중부양 후 시계방향으로 90도 돌려서 쌓기
    len_check = False
    while 1:
        # 쌓기 시작할 위치 찾기
        stack = 0
        for i in range(len(fish) - 1, -1, -1):
            if len(fish[i]) > 1:
                # 쌓는 길이가 남는 길이보다 커진다면 종료
                if len(fish[i]) > len(fish) - 1 - i:
                    len_check = True
                stack = i + 1
                break
        # 반복문 종료
        if len_check == True:
            break
        # 시계방향으로 돌려서 쌓기
        for i in range(stack - 1, -1, -1):
            if fish[i]:
                for j in range(len(fish[i])):
                    stack_fish = fish[i].pop(0)
                    fish[stack + j].append(stack_fish)

    move_checked = fish_move(N, fish)
    for r in range(N):
        for c in range(N):
            if move_checked[r][c]:
                fish[r][c] += move_checked[r][c]

    # 일렬로 만들기
    line()

    count = 0
    # 절반 공중부양 회전작업 2번 시행
    stack = (N + 1) // 2
    for i in range(stack - 1, -1, -1):
        move_fish = fish[i].pop(0)
        fish[stack].append(move_fish)
        stack += 1

    stack = (N + 1) // 2 + ((N + 1) // 2) // 2
    for i in range(stack - 1, 0, -1):
        if fish[i]:
            for j in range(len(fish[i])):
                move_fish = fish[i].pop()
                fish[stack].append(move_fish)
            stack += 1

    move_checked = fish_move(N, fish)
    for r in range(N):
        for c in range(N):
            if move_checked[r][c]:
                fish[r][c] += move_checked[r][c]

    # 일렬로 만들기
    line()

    max_fish = 0
    min_fish = 123456789
    for i in range(len(fish)):
        max_fish = max(max_fish, fish[i][0])
        min_fish = min(min_fish, fish[i][0])

    if max_fish - min_fish <= K:
        break
    else:
        result += 1

print(result)