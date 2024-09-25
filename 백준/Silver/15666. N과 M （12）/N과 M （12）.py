import sys
input = sys.stdin.readline
def backtrack(part,index):
    global numbers
    global m , n
    if len(part) == m:
        print(' '.join(map(str,part)))
        return
    
    for i in range(len(numbers)):
        if index == 0 or index > 0 and part[-1] - 1 < numbers[i]:
            part.append(numbers[i])
            backtrack(part,i)
            part.pop()

n , m = map(int,input().split())
numbers = list(set(map(int,input().split())))
numbers.sort()

backtrack([],0)
