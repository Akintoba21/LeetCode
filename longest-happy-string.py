class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a: heappush(heap,(-a,'a'))
        if b: heappush(heap,(-b,'b'))
        if c: heappush(heap,(-c,'c'))
        r = ""
        prev = None
        pc = 0
        while heap and (not prev or prev != r):
            prev = r
            x,y = heappop(heap)
            if pc == 2 and y == r[-1]:
                if not heap: break
                pc = 0
                tx,ty = heappop(heap)
                r = r + ty
                if tx < -1: heappush(heap,(tx+1,ty))
            if not pc or r[-1] == y: pc += 1
            else: pc = 1
            r = r + y
            if x < -1: heappush(heap,(x+1,y))
        return r