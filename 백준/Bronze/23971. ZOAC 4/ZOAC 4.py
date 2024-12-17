h,w,n,m = map(int,input().split())

temp1 = h / (n+1)
if int(temp1) < float(temp1):
    temp1 = int(temp1) + 1
temp2 = w / (m+1)
if int(temp2) < float(temp2):
    temp2 = int(temp2) + 1
print(int(temp1*temp2))