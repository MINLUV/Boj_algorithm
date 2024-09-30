def modular_exponentiation(A, B, C):
    # B가 0이면 A^0은 항상 1
    if B == 0:
        return 1
    # B가 1이면 A를 C로 나눈 나머지를 반환
    if B == 1:
        return A % C
    
    # 재귀적으로 B를 반으로 나눠서 거듭제곱 계산
    half = modular_exponentiation(A, B // 2, C)
    half = (half * half) % C
    
    # B가 홀수일 경우 추가적으로 A를 곱해줘야 함
    if B % 2 == 1:
        half = (half * A) % C
    
    return half

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(modular_exponentiation(A, B, C))
