import sys

def gcd(a,b):
    if a > b:
        while b != 0:
            a,b = b,a%b
        return a
    elif a < b:
        while a != 0:
            b,a = a,b%a
        return b
    else:
        return a

t = int(sys.stdin.readline())

for _ in range(t):
    result = 0
    n = list(map(int,sys.stdin.readline().split()))
    for i in range(1,n[0]):
        for j in range(i+1,n[0]+1):
            result += gcd(n[i],n[j])
    print(result)



