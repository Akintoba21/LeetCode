class Solution:
    def minLength(self, s: str) -> int:
        l = len(s)
        s=s.replace('AB','')
        s=s.replace('CD','')
        while l != len(s):
            l = len(s)
            s=s.replace('AB','')
            s=s.replace('CD','')
        return len(s)