class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        r = []
        s1,s2 = s1.split(" "),s2.split(" ")
        for x in range(len(s1)):
            if s1.count(s1[x]) == 1 and s1[x] not in s2:
                r.append(s1[x])
        for x in range(len(s2)):
            if s2.count(s2[x]) == 1 and s2[x] not in s1:
                r.append(s2[x])
        return r