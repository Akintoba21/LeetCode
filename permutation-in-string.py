class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = len(s1)
        c = [s1.count(x) for x in s1]
        lc = len(c)
        l = 0
        while i < len(s2)+1:
            for x in range(lc):
                if c[x] != s2[l:i].count(s1[x]):
                    break
                if x == lc - 1: return True
            l += 1
            i += 1
        return False