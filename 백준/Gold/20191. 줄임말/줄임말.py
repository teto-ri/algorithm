from bisect import bisect_right, bisect_left

if __name__ == '__main__':
    s = input()
    t = input()
    # s = 'caa'
    # t = 'ac'
    next = [[] for _ in range(26)]
    for i in range(len(t)):
        next[ord(t[i]) - ord('a')].append(i)


    def solution(ss):
        ans = 1
        pos = -1
        before_pos = -1

        for y in ss:
            k = ord(y) - ord('a')
            if not next[k]:
                return -1

            pos = bisect_right(next[k], before_pos)
            if pos == len(next[k]):
                ans += 1
                pos = 0

            before_pos = next[k][pos]

        return ans


    if s == t:
        print(1)
    else:
        print(solution(s))