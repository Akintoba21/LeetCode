class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = len(grid)
        r = [-1,-1]
        for x in range(1, l*l+1):
            n = 0
            for y in grid:
                n += y.count(x)
            if n == 0:
                r[1] = x
            elif n == 2:
                r[0] = x
        return r