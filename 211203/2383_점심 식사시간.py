import sys
sys.stdin = open('2383_점심 식사시간.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    persons = []
    stairs = []
    result = 987654321

    for r in range(N):
        for c in range(N):
            if arr[r][c] > 1:
                stairs.append((r, c, arr[r][c]))
            if arr[r][c] == 1:
                persons.append((r, c))

    num_persons = len(persons)

    # 완전 탐색
    for i in range(1 << num_persons):
        # 각 사람이 어떤 계단에 가는지 저장
        tmp_stairs_person = [0] * num_persons
        for j in range(num_persons):
            if i & (1 << j):
                tmp_stairs_person[j] = 1

        # 각 사람이 배정받은 계단까지의 거리 저장
        tmp_dist_stair_person = [0] * num_persons
        for k in range(num_persons):
            person = persons[k]
            stair = stairs[tmp_stairs_person[k]]
            tmp_dist_stair_person[k] = abs(stair[0] - person[0]) + abs(stair[1] - person[1])

        # 정렬된 리스트
        stairs_person = [0] * num_persons
        dist_stair_person = [0] * num_persons
        tmp = 0
        while tmp_dist_stair_person:
            min_num = min(tmp_dist_stair_person)
            min_num_idx = tmp_dist_stair_person.index(min_num)

            stairs_person[tmp] = tmp_stairs_person.pop(min_num_idx)
            dist_stair_person[tmp] = tmp_dist_stair_person.pop(min_num_idx)

            tmp += 1

        # 모든 사람이 계단을 내려갈때까지 시간 계산
        # 계단을 이용중인 상태 표시 / 계단의 길이 삽입용
        stair_using = [[0] * num_persons, [0] * num_persons]
        # 해당 계단을 이용중인 사람 표시
        stair_using_num = [0, 0]
        # 계단 입구에서 대기중인 사람 표시 / 대기중인 사람은 1로 표시
        stair_waiting = [[0] * num_persons, [0] * num_persons]

        total_time = 0
        while True:
            if result <= total_time:
                break

            # 사람과 계단 사이의 거리가 모두 -2 이고
            # waiting이 비어있고
            # 계단을 이용중인 사람이 없다면 종료
            if dist_stair_person == [-2] * num_persons:
                if stair_waiting == [[0] * num_persons, [0] * num_persons]:
                    if stair_using_num == [0, 0]:
                        if result > total_time:
                            result = total_time
                        break

            for person_idx in range(num_persons):
                # 현재 사람이 이용하는 계단번호
                person_stair = stairs_person[person_idx]
                # 현재 사람이 계단과 남은거리가 -2보다 크다면
                if dist_stair_person[person_idx] > -2:
                    dist_stair_person[person_idx] -= 1

                if dist_stair_person[person_idx] == -2:
                    # 내가 기다리는 사람이 아니면
                    if stair_waiting[person_stair][person_idx] == 0:
                        # 한칸 내려가기
                        stair_using[person_stair][person_idx] -= 1
                        # 전부 내려갔다면
                        if stair_using[person_stair][person_idx] == 0:
                            # 해당 계단 이용중인 사람 -1
                            stair_using_num[person_stair] -= 1

                    # 내가 기다리는 사람이면
                    if stair_waiting[person_stair][person_idx] == 1:
                        # 계단을 이용할 수 있다면
                        if stair_using_num[person_stair] < 3:
                            # waitng 초기화 / 계단 진입
                            stair_waiting[person_stair][person_idx] = 0
                            stair_using[person_stair][person_idx] = stairs[person_stair][2]
                            stair_using_num[person_stair] += 1
                        # 계단을 이용할 수 없다면면
                        else:
                            continue

                if dist_stair_person[person_idx] == -1:
                    # 계단을 이용할 수 있다면
                    if stair_using_num[person_stair] < 3:
                        # 계단 진입
                        stair_using[person_stair][person_idx] = stairs[person_stair][2]
                        stair_using_num[person_stair] += 1
                    # 계단을 이용할 수 없다면
                    else:
                        # waiting 추가
                        stair_waiting[person_stair][person_idx] = 1

            total_time += 1

    print(f'#{tc} {result}')