import collections

x, y = map(int, input().split())

laddersnake = dict()
for i in range(x + y):
    a, b = map(int, input().split())
    laddersnake[a] = b

mincount = float('inf')
queue = collections.deque()
visited = set()  # 방문한 위치를 기록할 set
queue.append((1, 0))
visited.add(1)  # 시작 위치를 방문한 것으로 표시

while queue:
    now, count = queue.popleft()
    if now >= 100:
        mincount = count
        break
    else:
        for i in range(1, 7):
            next_pos = now + i
            if next_pos in laddersnake:
                next_pos = laddersnake[next_pos]
            if next_pos not in visited:  # 방문하지 않은 위치만 추가
                visited.add(next_pos)
                queue.append((next_pos, count + 1))

print(mincount)
