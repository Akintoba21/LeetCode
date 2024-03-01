class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        nlen = len(s) #length of string
        olen = s.count("1") #number of 1's
        zlen = nlen - olen #number of 0's
        return "1" * (olen-1) + "0" * zlen + "1"