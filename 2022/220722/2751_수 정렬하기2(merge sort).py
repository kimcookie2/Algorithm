def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 크기가 1이 될때까지 재귀호출
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j, k = 0, 0, 0

    # 비교 시작
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # 한쪽이 먼저 끝난다면 다른쪽도 마무리
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

    return arr

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

arr = merge_sort(arr)

for num in arr:
    print(num)