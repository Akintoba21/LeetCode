import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)
        r = 0
        for _ in range(k):
            x = -(heapq.heappop(h))
            r += x
            heapq.heappush(h,(x//-3))
        return r