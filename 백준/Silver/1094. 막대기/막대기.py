# 입력 받기
X = int(input())

# 막대 개수를 세기 위한 변수
count = 0

# 막대의 합이 X가 될 때까지 반복
while X > 0:
    # X의 가장 오른쪽 비트가 1이면 count 증가
    if X % 2 == 1:
        count += 1
    # X를 오른쪽으로 한 비트 이동
    X //= 2

# 결과 출력
print(count)
