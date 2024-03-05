class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        max_score = 0
        score = 0
        while(len(tokens) > 0):
            played = False
            temp = min(tokens)
            if(power >= temp):
                score = score + 1
                if(score > max_score):
                    max_score = score
                power = power - temp
                tokens.remove(temp)
                played = True
            else:
                temp = max(tokens)
                if(score > 0):
                    score = score - 1
                    power = power + temp
                    tokens.remove(temp)
                    played = True
            if(played == False):
                break
        return max_score