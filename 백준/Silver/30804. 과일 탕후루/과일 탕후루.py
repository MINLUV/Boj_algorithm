def max_fruit_length(n, fruits):
    max_len = 0
    left = 0
    fruit_count = {}
    
    for right in range(n):
        if fruits[right] in fruit_count:
            fruit_count[fruits[right]] += 1
        else:
            fruit_count[fruits[right]] = 1
            
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
            
        max_len = max(max_len, right - left + 1)
    
    return max_len

# 입력 처리
n = int(input())
fruits = list(map(int, input().split()))

# 결과 출력
print(max_fruit_length(n, fruits))
