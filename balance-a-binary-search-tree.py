# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.nodes = []

        def inorder(n):
            if n == None:
                return
            inorder(n.left)
            self.nodes.append(n)
            inorder(n.right)
        
        inorder(root)
        
        def buildTree(start, end):
            if start > end:
                return None
            mid = (start+end)//2
            newroot = self.nodes[mid]
            newroot.left = buildTree(start, mid-1)
            newroot.right = buildTree(mid+1,end)
            return newroot
        
        return buildTree(0, len(self.nodes)-1)