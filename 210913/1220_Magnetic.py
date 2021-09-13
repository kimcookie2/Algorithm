import sys
sys.stdin = open('1220_Magnetic.txt', 'r')

for tc in range(1, 11):
    length = int(input())
    arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    cnt = 0

    # Stack에 자성체를 순서대로 쌓기
    for j in range(100):
        Stack = []
        top = -1
        for i in range(100):
            if top + 1 == 0 and arr[i][j] == 2:
                pass
            elif arr[i][j] != 0:
                top += 1
                Stack.append(arr[i][j])

        # Stack이 비어있지 않다면, Stack[top]값이 1일때 제거
        if top != -1:
            while Stack[top] == 1:
                Stack.pop(top)
                top -= 1


        # Stack에 원소가 없을때까지 반복
        while len(Stack) != 0:
            # 우선적으로 2를 다 제거하고
            while Stack[top] == 2:
                Stack.pop()
                top -= 1
            # 그 뒤에 오는 1을 다 제거했을 때, 교착 상태 하나 증가
            while Stack[top] == 1:
                Stack.pop()
                top -= 1
                if top < 0:
                    break
            cnt += 1

    print(f'#{tc} {cnt}')