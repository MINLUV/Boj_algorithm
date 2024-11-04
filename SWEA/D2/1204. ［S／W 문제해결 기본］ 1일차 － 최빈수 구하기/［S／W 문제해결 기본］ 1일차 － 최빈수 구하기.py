test = int(input())

for testcase in range(1,test+1):
    a = int(input())

    lst = list(map(int,input().split()))
    dic = dict()
    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_ = 0
    maxpoint = 0
    for i,j in dic.items():
        if max_ < j:
            max_ = j
            maxpoint = i
    print(f'#{testcase} {maxpoint}')
