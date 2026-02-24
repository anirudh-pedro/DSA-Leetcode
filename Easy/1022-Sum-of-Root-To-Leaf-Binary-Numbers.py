# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.s = 0
        def back(root,bi):
            if not root:
                return
            bi += str(root.val)
            if not root.left and not root.right:
                k = int(bi,2)
                self.s += k
                return
            back(root.left,bi)
            back(root.right,bi)
        back(root,"")
        return self.s
