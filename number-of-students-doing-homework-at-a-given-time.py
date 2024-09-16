class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        r = 0
        for x in range(len(startTime)):
            r += (queryTime >= startTime[x] and queryTime <= endTime[x])
        return r