import sys
sys.stdin = open('1860_진기의 최고급 붕어빵.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    # 마지막 사람이 도착할 시간이 최대로 붕어빵을 만들고 있을 시간
    max_second = data[-1]
    # 시간별로 빵이 얼마나 있는지 저장
    maked_bread = [0] * (max_second + 1)

    # 시간별로 빵의 개수를 누적
    for i in range(1, len(maked_bread)):
        if i % M == 0:
            maked_bread[i] = maked_bread[i - 1] + K
        else:
            maked_bread[i] = maked_bread[i - 1]

    # 사람이 방문했을때
    for person in data:
        # 그 시간에 빵이 1개 이상 남아있다면
        if maked_bread[person] >= 1:
            # 이후의 시간대의 빵을 전부 하나씩 제거
            for i in range(person, len(maked_bread)):
                maked_bread[i] -= 1

        # 남아있는 빵이 없다면 불가능
        else:
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')