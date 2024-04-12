class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        m = max(height)
        mind = height.index(m)
        lmax = 0
        for i in range(mind):
            cur = height[i]
            if cur >= lmax:
                lmax = cur
                continue
            temp = lmax - cur
            if temp > 0: water += temp
            print("left", cur, lmax, water)

        rmax = 0
        for i in range(1, len(height) - mind):
            cur = height[-i]
            if cur >= rmax:
                rmax = cur
                continue
            temp = rmax - cur
            if temp > 0: water += temp
            print("right", cur, rmax, water)

        return water