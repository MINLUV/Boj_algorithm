def maximize_money(money, swaps_left, visited):
    global max_money
    current_money = int(''.join(map(str, money)))

    # 중복 방문 체크: money와 남은 swap 횟수를 함께 키로 사용
    if (current_money, swaps_left) in visited:
        return
    visited.add((current_money, swaps_left))

    # 남은 교환 횟수가 없으면 최대값 갱신
    if swaps_left == 0:
        max_money = max(max_money, current_money)
        return

    # 숫자판의 모든 가능한 교환을 시도
    n = len(money)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # i와 j를 교환
            money[i], money[j] = money[j], money[i]
            # 재귀 호출로 다음 교환 단계로 진행
            maximize_money(money, swaps_left - 1, visited)
            # 원래 상태로 되돌리기 (백트래킹)
            money[i], money[j] = money[j], money[i]

test_cases = int(input())

for testcase in range(1, test_cases + 1):
    money, num_swaps = input().split()
    money = list(map(int, money))
    num_swaps = int(num_swaps)
    
    # 최대 금액 초기화 및 방문 체크용 set 생성
    max_money = 0
    visited = set()
    
    # 재귀 탐색 시작
    maximize_money(money, num_swaps, visited)
    
    print(f"#{testcase} {max_money}")
