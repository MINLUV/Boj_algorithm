number = list(map(int,input().split()))
out = False
for i in range(1,1000001):
    count = 0
    if not out:
        for j in range(len(number)):
            if i%number[j] == 0:
                count += 1
            if count > 2:
                print(i)
                out = True
                break
