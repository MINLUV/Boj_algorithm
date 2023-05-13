import collections
def solution(nums):
    count = collections.Counter(nums)
    max = len(nums)/2
    print(collections.Counter(nums))
    if len(count) > max:
        answer = max
    else:
        answer = len(count)
    return answer