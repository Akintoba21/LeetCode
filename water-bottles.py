class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        r = numBottles
        while numBottles >= numExchange:
            r += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)
        return r