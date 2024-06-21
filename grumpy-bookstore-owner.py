class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        r = 0
        sat = 0
        for x in range(minutes):
            sat += customers[x]
        for x in range(minutes, len(customers)):
            if grumpy[x] == 0:
                sat += customers[x]
        r = sat
        for x in range(minutes, len(customers)):
            if grumpy[x] == 1:
                sat += customers[x]
            if grumpy[x-minutes] == 1:
                sat -= customers[x-minutes]
            if sat > r:
                r = sat
        return r