import sys
sys.stdin = open('3499_퍼펙트 셔플.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    shuffle = [0] * N

    if N % 2 == 0:
        deck_top = N // 2
    else:
        deck_top = (N // 2) + 1

    i = 0
    j = 0
    while j < deck_top:
        shuffle[i] = cards[0 + j]
        if (i + 1) < N:
            shuffle[i + 1] = cards[deck_top + j]
        i += 2
        j += 1

    print(f'#{tc} {" ".join(shuffle)}')