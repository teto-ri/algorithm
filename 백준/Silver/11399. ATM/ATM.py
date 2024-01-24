import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))

time_list = [0] * N

for i in range(1,N):
    in_idx = i
    in_val = n[i]
    for j in range(i-1,-1,-1):
        if n[j] < n[i]:
            in_idx = j+1
            break
        if j == 0:
            in_idx = 0
    for j in range(i,in_idx,-1):
        n[j] = n[j-1]
    n[in_idx] = in_val
time_list[0] = n[0]
for i in range(1,N):
    time_list[i] = time_list[i-1] + n[i]
print(sum(time_list))