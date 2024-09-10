import collections
x , y = map(int,input().split())

laddersnake = dict()

queue = collections.deque()
for i in range(x+y):
    a,b = map(int,input().split())
    laddersnake[a] = b

mincount = float('inf')
queue.append((1,0))
visited = set()
visited.add(1)
while queue:
    now , count = queue.popleft()
    if now >= 100:
        mincount = count
        break
    
    for i in range(1,7):
        next = now + i
        if next in laddersnake:
            next = laddersnake[next]
    
        if next not in visited:
            visited.add(next)
            queue.append((next,count+1))
print(mincount)