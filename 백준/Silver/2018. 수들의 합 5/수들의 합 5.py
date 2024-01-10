import sys
input = sys.stdin.readline
N = int(input())
cnt = 1
s = 1
e = 1
sum = 1

while e != N:
    if sum == N:
        cnt +=1
        e+=1
        sum+=e
    elif sum > N:
        sum-=s
        s+=1
    else:
        e+=1
        sum+=e
print(cnt)