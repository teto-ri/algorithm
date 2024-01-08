first_x = x = int(input())
count = 0
while True:
    x1 = x // 10
    x2 = x % 10
    x3 = (x1+x2) % 10
    x = int(str(x2)+str(x3))
    count+=1
    if first_x == x:
        break
print(count)