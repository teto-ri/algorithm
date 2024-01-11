import sys
input = sys.stdin.readline
N = int(input())
n = list(map(int,input().split()))
n = sorted(n)
cnt = 0

for idx in range(N):
    number = n[idx]
    s = 0
    e = N-1
    while s < e:
        if n[s] + n[e] == number:
            if s != idx and e != idx:
                cnt += 1
                break
            elif s == idx:
                s += 1
            elif e == idx:
                e -= 1
        elif n[s] + n[e] < number:
            s += 1
        else:
            e -= 1
print(cnt)