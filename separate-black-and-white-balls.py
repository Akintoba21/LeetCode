class Solution:
    def minimumSteps(self, s: str) -> int:
        nz = 0
        r = 0
        for x in s[::-1]:
            if x == '0': nz += 1
            else: r += nz
        return r 