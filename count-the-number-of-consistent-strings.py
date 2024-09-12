class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        r = 0
        for x in words:
            c = True
            for y in x:
                if y not in allowed:
                    c = False
                    break
            if c: r += 1
        return r