def backtracking(n, m, path, visited, numbers):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 경우에만 진행
            visited[i] = True
            path.append(numbers[i])
            backtracking(n, m, path, visited, numbers)
            path.pop()  # 백트래킹: path에서 마지막 요소 제거
            visited[i] = False

if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()  # 사전 순 출력을 위해 정렬
    visited = [False] * n
    backtracking(n, m, [], visited, numbers)
