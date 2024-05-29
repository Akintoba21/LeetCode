class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        difs = []
        for x in range(len(s)):
            dif = abs(ord(s[x]) - ord(t[x]))
            difs.append(dif)
        lind = 0
        rind = 0
        r = 0
        while lind < len(difs) and rind < len(difs):
            if sum(difs[lind:rind]) + difs[rind] <= maxCost:
                rind += 1
            else:
                if (rind - lind) > r:
                    r = rind - lind
                lind += 1
                if(lind > rind): rind = lind
        if (rind - lind) > r:
            r = rind - lind
        return r