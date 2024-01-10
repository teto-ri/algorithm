import sys
input = sys.stdin.readline
S = int(input())
cnt = 0
n = 1
sum = 0
while sum<=S:
    sum+=n
    cnt+=1
    n+=1
print(cnt-1)