import sys
input = sys.stdin.readline

def lis_length(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# 입력 처리
n = int(input())
number = list(map(int, input().split()))

# 최장 증가 부분수열의 길이를 계산
maxcount = lis_length(number)

print(maxcount)
