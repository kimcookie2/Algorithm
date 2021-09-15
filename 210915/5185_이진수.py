import sys
sys.stdin = open('5185_이진수.txt', 'r')

def binary(num):
    arr = [0] * 4
    t = 0
    while num >= 1:
        arr[t] = num % 2
        t += 1
        num = num // 2
    for i in range(3, -1, -1):
        print(arr[i], end='')

T = int(input())
for tc in range(1, T + 1):
    N, hexa = input().split()
    N = int(N)
    hexa_dict = {'A' : 10,
                 'B' : 11,
                 'C' : 12,
                 'D' : 13,
                 'E' : 14,
                 'F' : 15}

    print(f'#{tc} ', end='')

    for i in hexa:
        if str.isalpha(i):
            binary(hexa_dict[i])
        else:
            binary(int(i))

    print('')