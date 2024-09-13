a , b = map(int,input().split())
lst = list()
for i in range(1,b+1):
    for j in range(i):
        lst.append(i)
print(sum(lst[a-1:b]))