import collections

start , end = map(int,input().split())
mincount = float('inf')
count = 0
queue = [(start,0)]
queue = collections.deque(queue)
while queue:
    now , count = queue.popleft()
    if now == end:
        if count < mincount:
            mincount = count
    if now * 10 + 1 <= end:
        queue.append((now*10+1,count+1))
    if now * 2 <= end:
        queue.append((now*2,count+1))
if mincount == float('inf'):
    print(-1)
else:
    print(mincount+1)