n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

maxcnt = 0

for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for a in range(i,i+3):
            for b in range(j,j+3):
                if arr[a][b] == 1:
                    cnt += 1
        if cnt > maxcnt:
            maxcnt = cnt
print(maxcnt)
                