import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

# 트리를 인접 리스트 형태로 저장
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모를 저장할 배열
parent = [0] * (n + 1)

# BFS 탐색 시작
def bfs():
    queue = deque([1])  # 루트 노드부터 시작
    parent[1] = 1  # 루트의 부모는 자기 자신으로 설정
    while queue:
        node = queue.popleft()
        # 현재 노드의 자식 노드들을 순회
        for neighbor in graph[node]:
            if parent[neighbor] == 0:  # 방문하지 않은 노드라면
                parent[neighbor] = node  # 부모를 현재 노드로 설정
                queue.append(neighbor)

bfs()

# 2번 노드부터 부모를 출력
for i in range(2, n+1):
    print(parent[i])
