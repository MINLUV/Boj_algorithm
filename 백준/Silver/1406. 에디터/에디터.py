# -*- coding:utf-8 -*-
import sys

result = list(sys.stdin.readline().rstrip())
substack = []

T = int(input())
cursor = len(result)
for i in range(T):
    command = list(sys.stdin.readline().split())
    if(command[0] == 'L' and result != []):
        substack.append(result.pop())
    elif(command[0] == 'D' and substack != []):
        result.append(substack.pop())
    elif(command[0] == 'B' and result != []):
        result.pop()
    elif(command[0] == 'P'):    
        result.append(command[1])
print(''.join(result+list(reversed(substack))))