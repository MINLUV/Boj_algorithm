import itertools
test = int(input())

for testcase in range(1,test+1):
    number = int(input())
    temp = list(map(int,input().split()))
    point = []
    now = (temp[0],temp[1])
    end = (temp[2],temp[3])
    for i in range(4,number*2+4,2):
        point.append((temp[i],temp[i+1]))

    point = itertools.permutations(point)
    min_ = float('inf')
    for p in point:
        count = 0
        for i in range(number-1):
            count += abs(p[i][0]-p[i+1][0]) + abs(p[i][1]-p[i+1][1])

        count+= abs(now[0]-p[0][0]) + abs(now[1]-p[0][1])
        count+= abs(end[0]-p[-1][0]) + abs(end[1]-p[-1][1])
        if count < min_:
            min_ = count

    print(f'#{testcase} {min_}')