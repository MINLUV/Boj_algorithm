test = int(input())

for testcase in range(1,test+1):
    n , p = map(int,input().split())
    count = 0
    for i in range(1,n+1):
        if count + i != p:
            count += i
        else:
            count += i-1
        
    print(count)