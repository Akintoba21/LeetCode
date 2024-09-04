# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        temp = ""
        for y in range(len(traversal)):
            try:
                int(traversal[y])
                temp = temp + traversal[y]
            except: break
        root = TreeNode(temp)
        self.t = traversal[len(temp):]

        def bt(n, level):
            if len(traversal) <= 0:
                return
            if not n: return
            dash = 0
            temp = -1
            for x in range(len(self.t)):
                try:
                    int(self.t[x])
                    temp = self.t[x]
                    for y in range(x+1, len(self.t)):
                        try:
                            int(self.t[y])
                            temp = temp + self.t[y]
                        except: break
                    break
                except: dash += 1
            print(temp)
            if dash == level + 1:
                if not n.left: 
                    n.left = TreeNode(temp)
                    self.t = self.t[dash+len(temp):]
                    bt(n.left, level+1)
                else:
                    n.right = TreeNode(temp)
                    self.t = self.t[dash+len(temp):]
                    bt(n.right, level+1)
                bt(n,level)
            else:
                return
            
        bt(root,0)

        return root