class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        ilist = range(len(deck))
        deck.sort()
        r = [0] * len(deck)
        while len(deck) > 0:
            ind = ilist.pop(0)
            r[ind] = deck[0]
            deck.pop(0)
            if not len(ilist) > 0:
                continue
            temp = ilist.pop(0)
            ilist.append(temp)
        return r
