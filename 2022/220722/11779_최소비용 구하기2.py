def dijkstra(start):
    # 시작노드 : 시작노드 거리 계산 & 방문처리
    cost[start] = 0
    visited[start] = 1
    way.append(start)

    # graph에 도착할 수 있는 노드 탐색
    for end in range(len(graph[start])):
        if graph[start][end]:
            cost[end] = graph[start][end]

    # 시작노드를 제외한 n - 1개의 다른 노드 처리
    for _ in range(n - 1):
        # 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 탐색
        min_value = -123456789
        idx = 0
        for i in range(1, n + 1):
            if not visited[i] and cost[i] < min_value:
                min_value = cost[i]
                idx = i

        # 해당 노드 방문 처리
        visited[idx] = 1

        # 해당 노드의 인접한 노드들 간의 거리를 계산
        for next in range(len(graph[idx])):
            if graph[idx][next]:
                # 시작 -> now 거리 + now -> now의 인접노드 거리
                new_cost = cost[idx] + graph[idx][next]
                # new_cost < 시작 -> now의 인접노드 다이렉트 거리
                if new_cost < cost[next]:
                    cost[next] = new_cost

n = int(input())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost

start, end = map(int, input().split())

visited = [0] * (n + 1)
cost = [123456789] * (n + 1)
way = []

dijkstra(start)
print(way)
print(cost)