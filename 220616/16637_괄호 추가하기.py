import sys
from collections import deque
sys.stdin = open('input1.txt', 'r')

def pre_cal(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2

def calculate(n):
    global result

    if n == M:
        queue = deque(mathLine)
        new_queue = deque([])
        idx = 0
        while queue:
            if idx % 2 == 0:
                num = queue.popleft()
                new_queue.append(num)
                idx += 1
            else:
                m = (idx - 1) // 2
                if checked[m] == 0:
                    oper = queue.popleft()
                    new_queue.append(oper)
                    idx += 1
                else:
                    num1 = new_queue.pop()
                    oper = queue.popleft()
                    num2 = queue.popleft()
                    num3 = pre_cal(num1, oper, num2)
                    new_queue.append(num3)
                    idx += 2

        while len(new_queue) != 1:
            num1 = new_queue.popleft()
            oper = new_queue.popleft()
            num2 = new_queue.popleft()
            num3 = pre_cal(num1, oper, num2)
            new_queue.appendleft(num3)

        if new_queue[0] > result:
            result = new_queue[0]
        return

    if checked[n - 1] == 0:
        checked[n] = 1
        calculate(n + 1)
    checked[n] = 0
    calculate(n + 1)

N = int(input())
inputLine = input()
mathLine = [0] * N
result = -1 * 2 ** 32 - 1

for i in range(N):
    if i % 2 == 0:
        mathLine[i] = int(inputLine[i])
    else:
        mathLine[i] = inputLine[i]

M = N // 2
checked = [0] * M

calculate(0)

print(result)