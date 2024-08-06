from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word).most_common()
        letters = 0
        r = 0
        for x, y in c:
            letters += 1
            r += -(letters//-8) * y
        return r