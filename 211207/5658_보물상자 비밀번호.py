import sys
sys.stdin = open('5658_보물상자 비밀번호.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()
    code_length = int(N / 4)
    codes = []
    hex_to_dex = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    for rotation in range(code_length):
        for start in range(0, N, code_length):
            code = ''
            for i in range(start, start + code_length):
                code += nums[(i + rotation) % N]

            hexa_code = 0
            for idx in range(code_length):
                hexa_code += (16 ** (code_length - idx - 1)) * hex_to_dex[code[idx]]

            if hexa_code not in codes:
                codes.append(hexa_code)


    codes = sorted(codes, reverse=True)

    print(f'#{tc} {codes[K - 1]}')