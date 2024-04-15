# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0

        def recurse(noder, num):
            if noder == None: return
            num += str(noder.val)
            if noder.left == None and noder.right == None:
                self.s += int(num)
                print self.s
                return
            recurse(noder.left, num)
            recurse(noder.right, num)

        recurse(root, "")
        return self.s