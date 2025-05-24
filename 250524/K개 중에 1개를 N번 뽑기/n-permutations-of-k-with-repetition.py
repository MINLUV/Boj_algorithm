

K, N = map(int, input().split())
arr = [i for i in range(K+1)]
result = []


def getnum(cur, size):
    global result
    if size >= N:
        temp = " ".join(map(str,result))
        print(temp)
        return

    for i in range(1,K+1):
        result.append(arr[i])
        getnum(cur,size+1)
        result.pop()

    return


#for i in range(1, K):
getnum(1,0)



# Please write your code here.
