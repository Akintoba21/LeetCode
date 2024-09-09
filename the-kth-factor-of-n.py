import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        facs = []
        for x in range(1,int(math.sqrt(n) + 1)):
            if n%x == 0: 
                facs.append(x)
                if not n//x == x: facs.append(n//x)
        if len(facs) < k: return -1
        facs.sort()
        return facs[k-1]