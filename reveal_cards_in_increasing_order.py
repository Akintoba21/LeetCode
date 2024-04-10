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
            r[ilist[0]] = deck[0]
            ilist.remove(ilist[0])
            deck.remove(deck[0])
            if not len(ilist) > 0:
                continue
            temp = ilist.pop(0)
            ilist.append(temp)
        return r