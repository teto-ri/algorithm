import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
sum_result = [0]
sum = 0
result = []
for i in num:
    sum += i
    sum_result.append(sum)
for i in range(M):
    a,b = map(int,input().split())
    result.append(sum_result[b]-sum_result[a-1])
for i in result:
    print(i)
