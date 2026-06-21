# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(node, curmax):
    if node is None:
        return 0
    if node.val >= curmax:
        return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
    else:
        return dfs(node.left, curmax) + dfs(node.right, curmax)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root, -101)