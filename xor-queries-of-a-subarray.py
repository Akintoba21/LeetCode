class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ps = []
        n = 0
        for x in arr:
            n = n ^ x
            ps.append(n)
        r = []
        for x in queries:
            temp = ps[x[1]]
            if x[0] != 0:
                temp = temp ^ ps[x[0]-1]
            r.append(temp)
        return r