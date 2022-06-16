import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
nums = []

for i in range(N):
    tmp = int(sys.stdin.readline())

    if i == 0:
        nums.append(tmp)
        print(nums[0])
        continue

    for j in range(i):
        if j == i - 1 or nums[j] >= tmp:
            nums.insert(j, tmp)
            break

    center = int(i / 2)
    if (i + 1) % 2 == 1:
        print(nums[center])
    else:
        print(min(nums[center], nums[center + 1]))