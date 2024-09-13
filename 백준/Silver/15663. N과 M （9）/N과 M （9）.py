def backtrack(part,visited):
    global m
    global number
    if len(part) == m:
        print(' '.join(map(str,part)))
        return
    prev = -1
    for i in range(len(number)):
        if not visited[i] and number[i] != prev: 
            part.append(number[i])
            visited[i] = True
            backtrack(part,visited)
            visited[i] = False
            part.pop()
            prev = number[i]

    
    

n , m = map(int,input().split())
number = list(map(int,input().split()))
number = sorted(number)
visited = [False for _ in range(n)]
backtrack([],visited)


