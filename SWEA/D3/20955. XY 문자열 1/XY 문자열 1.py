test = int(input())

for testcase in range(1,test+1):
    start = input()
    end = input()

    while len(start) < len(end) :
        if end[-1] == 'X':
            end = end[:-1]
        elif end[-1] == 'Y':
            end = end[:-1][::-1]
    if start == end:
        print(f"#{testcase} Yes")
    else:
        print(f"#{testcase} No")
