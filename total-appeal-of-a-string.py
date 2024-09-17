class Solution:
    def appealSum(self, s: str) -> int:
        r = 0
        cur = 0
        prev = [-1] * 26
        for x in range(len(s)):
            print(r,cur)
            cur += x - prev[ord(s[x]) - ord("a")]
            prev[ord(s[x]) - ord("a")] = x
            r += cur
        return r    