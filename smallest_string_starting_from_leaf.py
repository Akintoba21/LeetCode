# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.smallest = ""
        
        def helper(node, s):
            news = chr(97 + node.val) + s
            if node.left == None and node.right == None:
                if (self.smallest == "" or news < self.smallest):
                    self.smallest = news
                return
            if node.left: helper(node.left, news)
            if node.right: helper(node.right, news)
            return
        
        helper(root, "")
        return self.smallest