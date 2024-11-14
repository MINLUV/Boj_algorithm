test = int(input())

for testcase in range(1,test+1):
    result = 0
    numbers = list(map(int,input().split()))

    for temp in numbers:
        if temp % 2 == 1:
            result += temp
    print(f"#{testcase} {result}")
    


