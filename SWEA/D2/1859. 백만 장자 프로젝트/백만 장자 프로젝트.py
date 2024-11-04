test = int(input())

for testcase in range(1,test+1):
    day = int(input())
    prices = list(map(int,input().split()))
    get = []
    count = 0
    while prices:
        maxprice = 0 
        maxindex = 0
        for i in range(len(prices)):
            if prices[i] > maxprice:
                maxprice = prices[i]
                maxindex = i

        for i in range(maxindex):
            count += maxprice - prices[i]
        
        prices = prices[maxindex+1:]
        
       
        
    print(f'#{testcase} {count}')
        