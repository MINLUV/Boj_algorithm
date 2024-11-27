a = input()
b = int(input())

a = int(a[:-2] + '00')


for i in range(100):
    if (a + i) % b == 0:
        break

if i < 10:
    print('0'+str(i))
else:
    print(i)
