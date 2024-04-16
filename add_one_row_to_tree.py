# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            nr = TreeNode(val)
            nr.left = root
            return nr
        def helper(n, count):
            if(n == None):return
            if count == depth-1:
                templ = TreeNode(val)
                templ.left = n.left
                n.left = templ
                tempr = TreeNode(val)
                tempr.right = n.right
                n.right = tempr
            helper(n.left, count+1)
            helper(n.right, count+1)
            return
        helper(root, 1)
        return root