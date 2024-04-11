class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        r = []
        for x in num:
            while len(r) > 0 and r[-1] > x and k > 0:
                r.pop()
                k = k - 1
            r.append(x)
        while k > 0:
            r.pop()
            k = k - 1
        r = "".join(r)
        if r == "": return "0"
        return str(int(r))