import sys
input = sys.stdin.readline

def maxvalue(count,value,visited,now):
    global paper
    global max_
    global row , col
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    visited[now[0]][now[1]] = True
    value += paper[now[0]][now[1]]
    count += 1

    if count == 1:
        tempvalue = []
        for i , j in direction: # 볼록할 척 모양의 테트로노미노만 계산.
            r , c  = now[0]+i , now[1]+j
            if -1 < r < row and -1 < c < col:
                tempvalue.append(paper[r][c])

        tempvalue.sort(reverse=True)
        tempsum = sum(tempvalue[0:3]) + value
        if tempsum > max_:
            max_ = tempsum

    if count == 4:
        if max_ < value:
            max_ = value
        visited[now[0]][now[1]] = False
        return

    for i , j in direction:
        r , c  = now[0]+i , now[1]+j
        if -1 < r < row and -1 < c < col and not visited[r][c]:
            maxvalue(count,value,visited,(r,c))
    visited[now[0]][now[1]] = False

row , col = map(int,input().split())
paper = list()
max_ = 0
visited = [[False for _ in range(col)] for _ in range(row)]

for i in range(row):
    paper.append(list(map(int,input().split())))

for i in range(row):
    for j in range(col):
        maxvalue(0,0,visited,(i,j))

print(max_)