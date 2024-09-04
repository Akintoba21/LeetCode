class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ns = ""
        for x in s:
            ns = ns + str(ord(x)-96)
        ns = list(map(int,ns))
        for _ in range(k):
            if len(ns) < 2: break
            n = sum(ns)
            ns = list(map(int,str(n)))
        return int(''.join(map(str, ns)))