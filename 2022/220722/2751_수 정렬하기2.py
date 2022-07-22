def quickSort(start, end):
    if start >= end:
        return

    pivot = arr[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= end and arr[i] < pivot:
            i += 1
        while j > start and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]

    quickSort(start, j - 1)
    quickSort(j + 1, end)

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = int(input())

quickSort(0, N - 1)

for num in arr:
    print(num)