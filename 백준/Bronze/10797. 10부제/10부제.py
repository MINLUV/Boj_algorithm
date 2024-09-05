cardict = dict()

n = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
    if i not in cardict:
        cardict[i] = 1
    else:
        cardict[i] += 1

if n in cardict:
    print(cardict[n])
else:
    print(0)