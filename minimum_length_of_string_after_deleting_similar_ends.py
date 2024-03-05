class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = len(s) - 1
        while(l < r and s[l] == s[r]):
            print(l,r)
            temp = s[l]
            while(l < len(s) and s[l] == temp):
                l = l + 1
            while(r > 0 and s[r] == temp):
                r = r - 1
            if(r < l):
                return 0
        return r - l + 1