class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0
        while True:
            for x in range(len(tickets)):
                if tickets[x] == 0: continue
                tickets[x] = tickets[x] - 1
                time = time + 1
                if tickets[x] == 0:
                    if x == k:
                        return time