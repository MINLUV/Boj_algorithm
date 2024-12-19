while True:
    a = int(input())
    count = 0
    if a == 0:
        break
    else:
        for i in range(1,a+1):
            count += i
    print(count)
