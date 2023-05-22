n,x = map(int,input().split())
arr = list(map(int,input().split()))
stack = []
for i in arr:
    if i < x:
        stack.append(str(i))
print(" ".join(stack))