import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

# 누적 합 배열 만들기
prefix_sum = [[0] * (n+1) for _ in range(n+1)]

# 누적 합 계산

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = box[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    # (x1, y1)부터 (x2, y2)까지의 구간 합 계산
    result = (prefix_sum[x2][y2] 
              - prefix_sum[x1-1][y2] 
              - prefix_sum[x2][y1-1] 
              + prefix_sum[x1-1][y1-1])
    
    print(result)
