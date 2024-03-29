from collections import defaultdict


def getLengthofLongestSubstring(k, s):
    i, j, n = 0, 0, len(s)
    mp = defaultdict(int)
    ans = 0

    while (i < n):
        ch = s[i]
        mp[ch] += 1
        while (len(mp) > k):
            ch1 = s[j]
            mp[ch1] -= 1
            if (mp[ch1] == 0):
                mp.pop(ch1)
            j += 1

        ans = max(ans, i-j+1)
        i += 1

    return ans


# Main Code.
t = int(input())

for i in range(t):
    k = int(input())
    s = input().strip()
    ans = getLengthofLongestSubstring(k, s)

    print(ans)
