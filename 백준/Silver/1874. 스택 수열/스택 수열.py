import sys
input = sys.stdin.readline

N = int(input())
P = [0]*N
for i in range(N):
    P[i] = int(input())
stack = []
num = 1
result = True
ans = ""

for i in range(N):
    now = P[i]
    if now >= num:
        while now >= num:
            stack.append(num)
            ans += "+\n"
            num += 1
        stack.pop()
        ans += "-\n"
    else:
        n = stack.pop()
        if n > now:
            print("NO")
            result = False
            break
        else:
            ans += "-\n"
            
if result:
    print(ans)
