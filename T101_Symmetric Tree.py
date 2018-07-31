# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Compare(self,one,two):
        """
        :param left:
        :param right:
        :return:
        """
        if one is None or two is None:
            return one == two
        return one.val == two.val and self.Compare(one.left, two.right) and \
               self.Compare(one.right, two.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return  self.Compare(root,root)


