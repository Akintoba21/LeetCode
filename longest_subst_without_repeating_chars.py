class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = ""
        for x in range(len(s)):
            y = x + 1
            temp = str(s[x])
            while y < len(s):
                if(s[y] in temp):
                    break
                temp = temp + s[y]
                y = y + 1
            if(len(temp) > len(r)):
                r = temp
        return len(r)