class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        nodes = []
        nodes.append(source)
        while True:
            if destination in nodes:
                return True
            print(nodes)
            temp = len(nodes)
            for e in edges:
                if e[0] in nodes:
                    if e[1] == destination:
                        return True
                    nodes.append(e[1])
                    edges.remove(e)
                elif e[1] in nodes:
                    if e[0] == destination:
                        return True
                    nodes.append(e[0])
                    edges.remove(e)
            if len(nodes) == temp: return False