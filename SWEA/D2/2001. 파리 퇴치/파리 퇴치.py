test = int(input())

for testcase in range(1,test+1):
    n , m = map(int,input().split())


    place = [list(map(int,input().split())) for _ in range(n)]
    max_ = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(i,i+m):
                for l in range(j,j+m):
                    temp += place[k][l]
            if temp > max_:
                max_ = temp
    print(f"#{testcase} {max_}")