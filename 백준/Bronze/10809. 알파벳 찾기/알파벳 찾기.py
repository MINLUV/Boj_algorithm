S = input()
result = [-1] * 26
count = 0
for i in S:
    count += 1
    if(result[ord(i)-97] == -1):
        result[ord(i)-97] += count

print(' '.join(map(str,result)))
