import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

# 입력 받기
city = int(input().strip())  # 도시의 개수
bus = int(input().strip())  # 버스의 개수

# 그래프 생성
graph = [[] for _ in range(city + 1)]
for _ in range(bus):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

# 시작 도시와 목적지 입력
start, end = map(int, input().split())

# 최소 비용 저장 테이블
dist = [INF] * (city + 1)
dist[start] = 0  # 시작점의 비용은 0으로 초기화

# 우선순위 큐 (비용, 현재 도시)
queue = []
heapq.heappush(queue, (0, start))

# 다익스트라 알고리즘 실행 (while 문 사용)
while queue:
    # 큐에서 최소 비용의 노드 선택
    current_cost, current_city = heapq.heappop(queue)
    
    # 이미 더 짧은 경로를 발견했다면 무시
    if dist[current_city] < current_cost:
        continue
    
    # 현재 도시에서 이동할 수 있는 경로 탐색
    for next_city, next_cost in graph[current_city]:
        total_cost = current_cost + next_cost
        
        # 더 짧은 경로를 발견하면 업데이트 및 큐에 추가
        if total_cost < dist[next_city]:
            dist[next_city] = total_cost
            heapq.heappush(queue, (total_cost, next_city))

# 목적지까지의 최소 비용 출력
print(dist[end])
