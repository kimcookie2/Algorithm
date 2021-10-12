import sys
sys.stdin = open('4012_요리사.txt', 'r')

def subset(k):
    global ans

    if k == N:
        if len(A) == len(B):
            tmp = synergy(A, B)
            if ans > tmp:
                ans = tmp

    else:
        A.append(k)
        subset(k + 1)
        A.pop()

        B.append(k)
        subset(k + 1)
        B.pop()

def synergy(A, B):
    result_A = 0
    result_B = 0

    for i in range(len(A)):
        for j in range(len(A)):
            result_A += arr[A[i]][A[j]]

    for i in range(len(B)):
        for j in range(len(B)):
            result_B += arr[B[i]][B[j]]

    return abs(result_A - result_B)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A, B = [0], []
    ans = 987654321
    subset(1)
    print(f'#{tc} {ans}')

