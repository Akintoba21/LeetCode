"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.r = []
        def rec(n):
            if not n: return
            for x in n.children:
                rec(x)
            self.r.append(n.val)
            return
        rec(root)
        return self.r