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

    # M개의 수식에 대해 괄호를 넣을 수 있는 모든 경우의 수 계산
    if n == M:
        queue = deque(mathLine)
        new_queue = deque([])
        idx = 0
        while queue:
            # 숫자는 항상 new_queue로 이동
            if idx % 2 == 0:
                num = queue.popleft()
                new_queue.append(num)
                idx += 1
            # 수식은 괄호 적용 여부에 따라 다르게 적용
            else:
                m = (idx - 1) // 2
                # 괄호를 적용하지 않는다면, 수식을 new_queue로 이동
                if checked[m] == 0:
                    oper = queue.popleft()
                    new_queue.append(oper)
                    idx += 1
                # 괄호를 적용해야 한다면, new_queue에 들어있던 숫자를 꺼내어 계산
                # 이후 계산된 숫자를 new_queue로 이동
                else:
                    num1 = new_queue.pop()
                    oper = queue.popleft()
                    num2 = queue.popleft()
                    num3 = pre_cal(num1, oper, num2)
                    new_queue.append(num3)
                    idx += 2

        # new_queue의 계산이 끝날때까지 순서대로 꺼내어 계산
        while len(new_queue) != 1:
            num1 = new_queue.popleft()
            oper = new_queue.popleft()
            num2 = new_queue.popleft()
            num3 = pre_cal(num1, oper, num2)
            new_queue.appendleft(num3)

        # 결과의 최대값을 저장
        if new_queue[0] > result:
            result = new_queue[0]
        return

    # 이웃한 수식끼리는 괄호가 들어가지 않도록 모든 경우의 수를 고려
    if checked[n - 1] == 0:
        checked[n] = 1
        calculate(n + 1)
    checked[n] = 0
    calculate(n + 1)

N = int(input())
inputLine = input()
mathLine = [0] * N
result = -1 * 2 ** 32 - 1

# 수식을 각각 문자열과 숫자로 받기
for i in range(N):
    if i % 2 == 0:
        mathLine[i] = int(inputLine[i])
    else:
        mathLine[i] = inputLine[i]

M = N // 2
# 몇 번째 수식에 괄호를 적용할 것인지 표시
checked = [0] * M

calculate(0)

print(result)