import sys
sys.stdin = open('1974_스토쿠 검증.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    puzzle = [0] * 9
    for i in range(9):
        puzzle[i] = list(map(int, input().split()))

    def sudoku(arr):
        for r in range(9):
            check = [0] * 9
            for c in range(9):
                check[arr[r][c] - 1] += 1
                if check[arr[r][c] - 1] > 1:
                    return 0

        for c in range(9):
            check = [0] * 9
            for r in range(9):
                check[arr[r][c] - 1] += 1
                if check[arr[r][c] - 1] > 1:
                    return 0

        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                check = [0] * 9
                for i in range(3):
                    for j in range(3):
                        check[arr[r + i][c + j] - 1] += 1
                        if check[arr[r + i][c + j] - 1] > 1:
                            return 0

        return 1

    print(f'#{tc} {sudoku(puzzle)}')