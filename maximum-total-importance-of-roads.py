import numpy

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cities = {}
        importance = [0] * (n)
        curimp = n

        for (x,y) in roads:
            if x not in cities:
                cities[x] = 1
            else: cities[x] += 1
            if y not in cities:
                cities[y] = 1
            else: cities[y] += 1
        
        keys = list(cities.keys())
        values = list(cities.values())
        sorted_value_index = numpy.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

        while len(sorted_dict) > 0:
            temp = sorted_dict.popitem()
            importance[temp[0]] = curimp
            curimp -= 1
        
        r = 0
        for (x,y) in roads:
            r += (importance[x] + importance[y])
            
        return r