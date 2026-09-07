# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return 0
        if root is not None:
            if root.left is not None and root.right is not None:
                if root.val==root.left.val+root.right.val:
                    return True
        return False
        