class Solution:
    def numTeams(self, rating: List[int]) -> int:
        r = 0

        for x in range(len(rating)):
            if x == 0:
                continue
            leftl = 0
            leftg = 0
            rightl = 0
            rightg = 0
            for y in range(0, x):
                if rating[y] < rating[x]: leftl += 1
                elif  rating[y] > rating[x]: leftg += 1
            for y in range(x+1, len(rating)):
                if rating[y] < rating[x]: rightl += 1
                elif  rating[y] > rating[x]: rightg += 1
            r += leftl * rightg
            r += leftg * rightl

        return r