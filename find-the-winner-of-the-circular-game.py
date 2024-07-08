class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        r = list(range(1,n+1))
        ind = 0
        count = 1
        if k == 1: return n
        while len(r) > 1:
            if count == k:
                r.pop(ind)
                if ind >= len(r): ind = 0
                count = 1
            ind += 1
            if ind >= len(r): ind = 0
            count += 1
        return r[0]