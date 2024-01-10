import sys
input = sys.stdin.readline
N, M = map(int,input().split())
n = list(map(int,input().split()))
sum_list = [0]
sum = 0

for i in n:
    sum += i
    sum_list.append(sum)

cnt = 0
s=0
e=1

while e<=N:
    sum = sum_list[e] - sum_list[s]
    if sum == M:
        cnt+=1
        e+=1
    elif sum > M:
        s+=1
    else:
        e+=1

print(cnt)