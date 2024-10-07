class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        r = 0
        l = len(strs[0])
        l1 = len(strs)
        for x in range(l):
            temp = strs[0][x]
            for y in range(1,l1):
                if temp > strs[y][x]:
                    r += 1
                    break
                temp = strs[y][x]
        return r