# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def helper(node, stack):
            if node is None:
                return
            if node.left:
                if node.right is not None:
                    stack.append(node.right)
                node.right = node.left
                node.left = None
            if node.right is None and stack:
                node.right = stack.pop()
            helper(node.right, stack)
            return
        helper(root, [])
        return


