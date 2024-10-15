n , m = map(int,input().split())

box = list(map(int,input().split()))
book = list(map(int,input().split()))

print(sum(box)-sum(book))