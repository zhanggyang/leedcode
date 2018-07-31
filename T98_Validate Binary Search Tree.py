# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BST(self,root,tem):
        if not root:return
        self.BST(self,root.left,tem)
        tem.append(root.val)
        self.BST(self,root.left,tem)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :判断搜索二叉树是否合法
        """
        L = [0]
        self.BST(self,root,L)
        for i in range(1,len(L)):
            if L[i]<L[i-1]:return False
        return True
        #搜索二叉树是合法



