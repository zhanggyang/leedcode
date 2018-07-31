# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Depth(self,root,depth):
        if not root:return depth-1
        return max(self.Depth(root.left,depth+1),\
                   self.Depth(root.right,depth+1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        return self.Depth(root,1)

