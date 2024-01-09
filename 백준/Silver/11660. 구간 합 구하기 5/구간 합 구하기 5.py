import sys
input = sys.stdin.readline
N,M = map(int,input().split())
sum_list = [[0]*(N+1) for _ in range(N+1)]
result = []
for i in range(N):
    num = list(map(int,input().split()))
    for j in range(N):
        sum_list[i+1][j+1] = sum_list[i][j+1] + sum_list[i+1][j] - sum_list[i][j] + num[j]

for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result.append(sum_list[x2][y2] - sum_list[x1-1][y2] - sum_list[x2][y1-1] + sum_list[x1-1][y1-1])
    
for i in result:
    print(i)