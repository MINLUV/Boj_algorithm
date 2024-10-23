import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    temp = input()
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    
    maxn = max(n_list) 
    maxm = max(m_list)

    if maxn >= maxm:
        print('S')
    elif maxn < maxm:
        print('B')
    else:
        print('C')
