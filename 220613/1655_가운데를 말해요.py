import sys
sys.stdin = open('input.txt', 'r')

import heapq

N = int(sys.stdin.readline())

leftHeap = []
rightHeap = []
answer = []

for i in range(N):
    inputNum = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-inputNum, inputNum))
    else:
        heapq.heappush(rightHeap, (inputNum, inputNum))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        smallNum = heapq.heappop(rightHeap)[0]
        largeNum = heapq.heappop(leftHeap)[1]

        heapq.heappush(leftHeap, (-smallNum, smallNum))
        heapq.heappush(rightHeap, (largeNum, largeNum))

    # print(-leftHeap[0])

    answer.append(leftHeap[0][1])

for j in answer:
    print(j)