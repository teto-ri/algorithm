import sys
input = sys.stdin.readline

N = int(input())
n = []

for i in range(N):
    n.append((int(input()),i))
n = sorted(n)
max=0
for i in range(N):
    if max < n[i][1]-i:
        max = n[i][1]-i
print(max+1)