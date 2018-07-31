# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Order(self,root,lever,res):
        if not root :return
        if len(res)<lever+1:res.append([])
        res[lever].append(root.val)
        self.Order(root.left,lever+1,res)
        self.Order(root.right,lever+1,res)
        return 

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.Order(root,0,res)
        return res


