people , party = map(int,input().split())

truthman = list(map(int,input().split()))
truthman = truthman[1:]
visited = [False for _ in range(party)]
partys = [list(map(int,input().split())) for _ in range(party)]

index= 0

while index < len(truthman):
    for i in range(party):
        if truthman[index] in partys[i][1:] and not visited[i]:
            visited[i] = True
            for a in partys[i][1:]:
                if a not in truthman:
                    truthman.append(a)
    index += 1

count = 0
for c in visited:
    if not c:
        count += 1

print(count)