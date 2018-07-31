# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Tree(self,preorder,inorder,root):
        if not preorder:
            del(root)
            return
        root.val = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:break
        if i>=1:
            root.left = TreeNode(0)
            self.Tree(self, preorder[1:i + 1], inorder[:i], root.left)
        if i<len(inorder)-1:
            root.right = TreeNode(0)
            self.Tree(self,preorder[i+1:],inorder[i+1:],root.right)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:return
        root = TreeNode(0)
        self.Tree(self,preorder,inorder,root)
        return root

    def pri(self,root):
        if not root:return 
        self.pri(self,root.left)
        print(root.val)
        self.pri(self,root.right)

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root= Solution.buildTree(Solution,preorder,inorder)
    Solution.pri(Solution,root)

