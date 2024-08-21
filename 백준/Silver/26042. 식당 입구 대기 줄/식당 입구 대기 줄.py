import sys
input = sys.stdin.readline

t = int(input())
maxlen = 0
maxlinestudent = sys.maxsize
count = 0

for i in range(t):
    command = list(map(int,input().split()))

    if command[0] == 1:
        count += 1
        if count > maxlen:
            maxlen = count
            maxlinestudent = command[1]  # 최대 길이를 갱신할 때만 학생 번호 갱신
        elif count == maxlen:
            maxlinestudent = min(maxlinestudent, command[1])  # 같은 길이일 때는 더 작은 학생 번호 선택

    elif command[0] == 2:
        count -= 1

print(maxlen, maxlinestudent)
