class Solution:
    def countSeniors(self, details: List[str]) -> int:
        r = 0
        for x in details:
            if int(x[11:13]) > 60:
                r += 1
        return r