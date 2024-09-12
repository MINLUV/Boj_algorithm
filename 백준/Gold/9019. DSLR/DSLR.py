from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    start , end = map(int,input().split())
    queue = deque(list())
    queue.append((start,''))
    visited = [False for _ in range(10000)]
    visited[start] = True
    while queue:
        now , command = queue.popleft()
        now = int(now)
        if now == end:
            print(command)
            break
        
        nextnum = now*2%10000
        if not visited[nextnum]:
            queue.append((nextnum,command + 'D'))
            visited[nextnum] = True
        
        nextnum = 9999 if now == 0 else now - 1
        if not visited[nextnum]:
            queue.append((nextnum,command+'S'))
            visited[nextnum] = True
        
    
        
        nextnum = now // 1000 + (now % 1000) * 10
        if not visited[nextnum]:
            visited[nextnum] = True
            queue.append((nextnum,command+'L'))

    
        
        nextnum = now // 10 + ( now % 10 ) * 1000
        if not visited[nextnum]:
            visited[nextnum] = True
            queue.append((nextnum,command+'R'))