# 첫째 줄에서 문자열의 총 개수 N을 입력받습니다.
N = int(input().strip())

# 이후 N개의 줄에서 각각의 문자열을 입력받고, 조건에 따라 결과를 출력합니다.
for _ in range(N):
    password = input().strip()
    # 비밀번호의 길이가 6 이상 9 이하인 경우 "yes", 그렇지 않으면 "no"를 출력합니다.
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print("no")
