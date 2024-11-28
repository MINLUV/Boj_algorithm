line = int(input())

dpmax = [0] * 3
dpmin = [0] * 3
play = list(map(int,input().split()))
dpmax[0] = play[0]
dpmax[1] = play[1]
dpmax[2] = play[2]
dpmin[0] = play[0]
dpmin[1] = play[1]
dpmin[2] = play[2]

for i in range(1,line):

    play = list(map(int,input().split())) 
    nextdpmax = [0] * 3
    nextdpmin = [0] * 3
    nextdpmax[0] = max(dpmax[0],dpmax[1]) + play[0]
    nextdpmax[1] = max(dpmax[0],dpmax[1],dpmax[2]) + play[1]
    nextdpmax[2] = max(dpmax[1],dpmax[2]) + play[2]
    nextdpmin[0] = min(dpmin[0],dpmin[1]) + play[0]
    nextdpmin[1] = min(dpmin[0],dpmin[1],dpmin[2]) + play[1]
    nextdpmin[2] = min(dpmin[1],dpmin[2]) + play[2]
    dpmax = nextdpmax
    dpmin = nextdpmin

print(max(dpmax[0],dpmax[1],dpmax[2]),min(dpmin[0],dpmin[1],dpmin[2]))
