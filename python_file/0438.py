from typing import List


def findAnagrams(self, s: str, p: str) -> List[int]:
    s_len = len(s)
    p_len = len(p)
    ans = []
    now = [0] * 26
    real = [0] * 26

    for i in range(p_len):
        real[ord(p[i]) - 97] += 1

    l, r = 0, 0
    while r < s_len:
        if r - l < p_len:
            now[ord(s[r]) - 97] += 1
            r += 1
        else:
            if (now == real):
                ans.append(l)
            now[ord(s[l]) - 97] -= 1
            l += 1
    if now == real:
        ans.append(l)
    return ans

s="cbaebabacd"
findAnagrams(s,"abc")

