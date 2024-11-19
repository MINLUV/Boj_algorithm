a , b = map(int,input().split())

c , d = map(int,input().split())

a1 = a + d
a2 = b + c

if a1 < a2:
    print(a1)
else:
    print(a2)