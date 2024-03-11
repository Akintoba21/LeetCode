class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        r = ""
        for x in order:
            c = s.count(x)
            for _ in range(c):
                r = r + x
        for x in s:
            if x in order:
                continue
            r = r + x
        return r