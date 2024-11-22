a , b = map(int,input().split())

d = list(map(int,input().split()))

for i in range(len(d)):
    print(d[i] - a*b ,end=' ') 

