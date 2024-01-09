import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
sum_list = []
sum = 0
result = 0
mod = 0
c = [0]*M
for i in num:
    sum += i
    sum_list.append(sum)
for i in range(N):
    mod = sum_list[i]%M
    if mod == 0:
        result += 1
    c[mod] += 1
for i in range(M):
    result += c[i]*(c[i]-1)//2
print(result)