import sys
sys.stdin = open("input1.txt", 'r')

def work(check, pre_node, ans):
    global result, k, n

    if check == k - 1:
        if ans < result:
            result = ans
            return

    if ans >= result:
        return

    if pre_node + 2 > n - 1:
        return

    for i in range(pre_node + 2, n - 1):
        new_ans = ans + lengths[i]
        work(check + 1, i, new_ans)

n, k = map(int, input().split())
companies = [0] * n
lengths = [0] * (n - 1)
visited = [0] * (n - 1)

for i in range(n):
    companies[i] = int(input())

for i in range(n - 1):
    lengths[i] = companies[i + 1] - companies[i]

result = 123456789

for i in range(n - 1):
    work(0, i, lengths[i])

print(result)