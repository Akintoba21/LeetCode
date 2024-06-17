class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l = list(range(0,int(math.sqrt(c)+1)))
        print(l)
        lptr = 0
        rptr = len(l) - 1
        while(rptr >= lptr):
            temp = (l[lptr] * l[lptr]) + (l[rptr] * l[rptr]) 
            if temp == c:
                return True
            elif temp < c:
                lptr += 1
            elif temp > c:
                rptr -= 1
        return False