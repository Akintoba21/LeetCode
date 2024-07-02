class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        prev = None
        ops = 0
        for x in word:
            pi = 0
            if prev: pi = ord(prev)
            ci = ord(x)
            changed = 0
            if pi == ci or pi - 1 == ci or pi + 1 == ci:
                ops += 1
                prev = None
                changed = 1
            if not changed:
                prev = x
        return ops