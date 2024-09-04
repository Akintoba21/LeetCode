class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set(map(tuple,obstacles))
        print(obstacles, obstacles_set)
        r = 0
        cd = 0
        p1, p2 = 0, 0
        for x in commands:
            if x == -2:
                cd -= 1
                if cd < 0:
                    cd = 3
            elif x == -1:
                cd += 1
                if cd > 3:
                    cd = 0
            else:
                if cd == 0:
                    for _ in range(x):
                        p2 += 1
                        if (p1,p2) in obstacles_set:
                            p2 -= 1
                            break
                elif cd == 1:
                    for _ in range(x):
                        p1 += 1
                        if (p1,p2) in obstacles_set:
                            p1 -= 1
                            break
                elif cd == 2:
                    for _ in range(x):
                        p2 -= 1
                        if (p1,p2) in obstacles_set:
                            p2 += 1
                            break
                elif cd == 3:
                    for _ in range(x):
                        p1 -= 1
                        if (p1,p2) in obstacles_set:
                            p1 += 1
                            break
            distance = (p1 * p1) + (p2 * p2)
            r = max(distance,r)
        return r