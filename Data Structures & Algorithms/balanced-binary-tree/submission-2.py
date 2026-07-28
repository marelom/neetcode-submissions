# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       left_depth = 0
       right_depth = 0
       self.balanced = True

       def helper(node):
        if node is None:
            return False

        left_depth = helper(node.left)
        right_depth = helper(node.right)

        difference = abs(left_depth - right_depth)

        if difference > 1:
            self.balanced = False   

        return max(right_depth, left_depth) + 1

       helper(root)

       return self.balanced
