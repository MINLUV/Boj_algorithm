while True:
    a, b, c = map(int,input().split())
    temp = [a,b,c]
    temp.sort()
    if a == 0:
        break
    else:
        if temp[2] > temp[1]+ temp[0] - 1 :
            print("Invalid")
        elif a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        elif a != b and b != c and a != c:
            print("Scalene")
            