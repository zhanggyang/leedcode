class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :中序遍历
        """
        res = []
        self.Traversal(self,root,res)
        return res

    def Traversal(self,root,List):
        if not root:return
        self.Traversal(self,root.left,List)
        if not root.val:
            List.append(root.val)
        self.Traversal(self,root.right,List)





