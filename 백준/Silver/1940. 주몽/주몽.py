import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
n = list(map(int,input().split()))
n = sorted(n)
cnt = 0
s = 0
e = N-1
while s < e:
    if n[s] + n[e] == M:
        cnt += 1
        s += 1
        e -= 1
    elif n[s] + n[e] < M:
        s += 1
    else:
        e -= 1
print(cnt)