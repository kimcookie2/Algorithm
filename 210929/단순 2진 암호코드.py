import sys
sys.stdin = open('단순 2진 암호코드.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    key = [['0', '0', '0', '1', '1', '0', '1'],
           ['0', '0', '1', '1', '0', '0', '1'],
           ['0', '0', '1', '0', '0', '1', '1'],
           ['0', '1', '1', '1', '1', '0', '1'],
           ['0', '1', '0', '0', '0', '1', '1'],
           ['0', '1', '1', '0', '0', '0', '1'],
           ['0', '1', '0', '1', '1', '1', '1'],
           ['0', '1', '1', '1', '0', '1', '1'],
           ['0', '1', '1', '0', '1', '1', '1'],
           ['0', '0', '0', '1', '0', '1', '1']]

    # 해석한 암호코드를 저장할 리스트
    code = []
    # 전체 암호코드를 저장할 리스트
    tmp = [0] * 56

    # 뒤에서 부터 탐색후 1이 나온다면, 그곳이 암호코드가 있는줄
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                for s in range(55, -1, -1):
                    tmp[s] = arr[i][j - 55 + s]
                # 첫 한줄만 찾으면 되므로 탐색 종료
                break

    # 암호코드를 앞에서부터 7개씩 짤라서 탐색
    for s in range(0, 56, 7):
        password = [0] * 7
        # 7개로 자른 암호코드를 새로운 리스트에 저장(비교를 위해)
        for i in range(7):
            password[i] = tmp[s + i]
        # 해당 암호코드와 일치하는 숫자를 찾아서 해석한 코드에 삽입
        for value in range(10):
            if key[value] == password:
                code.append(value)

    # 암호코드가 정상인지 검증
    result = (code[0] + code[2] + code[4] + code[6]) * 3 + (code[1] + code[3] + code[5]) + code[7]

    # 정상적인 암호코드라면 합을 출력
    if result % 10 == 0:
        print(f'#{tc} {sum(code)}')
    # 비정상적인 암호코드라면 0을 출력
    else:
        print(f'#{tc} 0')