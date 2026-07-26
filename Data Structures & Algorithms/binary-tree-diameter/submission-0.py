# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def helper(node):
            if node is None:
                return 0

            left_depth = helper(node.left)
            right_depth = helper(node.right)

            current_path = left_depth + right_depth
            self.longest = max(self.longest, current_path)

            return max(left_depth, right_depth) + 1

        helper(root)

        return self.longest        