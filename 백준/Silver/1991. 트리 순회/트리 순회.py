def func1(now):
    global nodes , node
    print(now,end='')
    if nodes[now][0] != '.':
        temp = nodes[now][0]
        func1(temp)
    if nodes[now][1] != '.':
        temp = nodes[now][1]
        func1(temp)
        
def func2(now,visited):
    global nodes, node
    visited.append(now)

    #왼쪽 자식 노드 방문 안한 경우 방문
    if nodes[now][0] not in visited:
        func2(nodes[now][0],visited)
    if nodes[now][0] in visited:
        print(now,end='')
    #오른쪽 자식 노드 방문 안한 경우 방문
    if nodes[now][1] not in visited:
        func2(nodes[now][1],visited)
    # 왼쪽 자식 노드와 오른쪽 자식 노드가 없을경우 루트 노드로 이동
    if nodes[now][0] in visited and nodes[now][1] in visited: 
        for key,value in nodes.items():
            if now in value:
                if key not in visited:
                    func2(key,visited)
                break
    
def func3(now,visited):
    global nodes, node
    visited.append(now)
        
    #왼쪽 자식 노드 방문 안한 경우 방문
    if nodes[now][0] not in visited:
        func3(nodes[now][0],visited)
        
    #오른쪽 자식 노드 방문 안한 경우 방문
    if nodes[now][1] not in visited:
        func3(nodes[now][1],visited)

    # 왼쪽 자식 노드와 오른쪽 자식 노드가 없을경우 루트 노드로 이동
    if nodes[now][0] in visited and nodes[now][1] in visited: 
        print(now,end='')
        for key,value in nodes.items():
            if now in value:
                if key not in visited:
                    func3(key,visited)
                break


if __name__ == '__main__':
    node = int(input())
    nodes = dict()
    for _ in range(node):
        root , left , right = map(str,input().split())
        nodes[root] = (left,right)
    func1('A')

    temp = 'A'
    while True:
        if nodes[temp][0] != '.':
            temp = nodes[temp][0]
        elif nodes[temp][0] == '.':
            break
    
    print()
    func2(temp,['.'])

    print()
    func3(temp,['.'])