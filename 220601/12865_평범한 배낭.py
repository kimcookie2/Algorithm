import sys
sys.stdin = open('input1.txt', 'r')

# 물품의 수 N, 버틸 수 있는 무게 K
N, K = map(int, input().split())
objects = [0] * N

# 계산 결과를 저장할 list
d = [[0] * (K + 1) for _ in range(N)]

for i in range(N):
    objects[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(K + 1):
        weight = objects[i][0]
        value = objects[i][1]

        # 현재 배낭에 들어갈 수 있는 무게보다 현재 넣을 물건의 무게가 크다면 넣지 않는다.
        if j < weight:
            d[i][j] = d[i - 1][j]

        # 그렇지 않다면 다음 중 더 높은 가치를 선택한다.
        # 1. 현재 물건을 넣지않고 이전 배낭을 그대로 가지고 간다.
        # 2. 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - weight] + value)

print(d[N - 1][K])
print(d)