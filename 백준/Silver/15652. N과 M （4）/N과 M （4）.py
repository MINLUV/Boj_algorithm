def backtrack(n, m, start, path):
    # 현재 path가 길이 m인 수열이 되면 출력
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    # start부터 n까지의 숫자를 차례로 시도
    for i in range(start, n + 1):
        # 현재 숫자를 path에 추가하고 재귀 호출
        backtrack(n, m, i, path + [i])

def solve():
    # N과 M을 입력 받음
    n, m = map(int, input().split())
    # 백트래킹 시작: 초기 상태는 숫자 1부터 시작하며, 빈 수열로 시작
    backtrack(n, m, 1, [])

# 실행
solve()
