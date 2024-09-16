class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for x in range(len(timePoints)):
            temp = timePoints[x].split(":")
            timePoints[x] = (int(temp[0])*60) + int(temp[1])
        timePoints.sort()
        prev = -1
        r = 1440
        for x in timePoints:
            if prev == -1:
                prev = x
                continue
            r = min(x-prev,r)
            r = min(r,(1440-x) + (timePoints[0]-0))
            prev = x
        return r