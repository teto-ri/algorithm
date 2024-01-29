import sys
input = sys.stdin.readline
ans = 0

N = int(input())
n = list(map(int,input().split()))
n.insert(0,0)
temp = [0]*(N+1)

def merge_sort(start,end):
    global ans
    if end-start < 1:
        return
    m = start + (end-start)//2
    merge_sort(start,m)
    merge_sort(m+1,end)
    for i in range(start,end+1):
        temp[i] = n[i]
    e = start
    j = start
    k = m+1
    while j <= m and k <= end:
        if temp[j] > temp[k]:
            n[e] = temp[k]
            ans = ans + k - e
            e += 1
            k += 1
        else:
            n[e] = temp[j]
            e += 1
            j += 1
    while j <= m:
        n[e] = temp[j]
        e += 1
        j += 1
    while k <= end:
        n[e] = temp[k]
        e += 1
        k += 1

merge_sort(1,N)
print(ans)