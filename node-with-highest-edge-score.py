class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for x in range(len(edges)):
            scores[edges[x]] += x
        r = 0
        rr = 0
        for x in range(len(scores)):
            if scores[x] > rr:
                rr = scores[x]
                r = x
        return r