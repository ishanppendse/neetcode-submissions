# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def insert(node, level):
    if node is not None:
        level.append(node)

def step(level):
    new_level = []
    for node in level:
        insert(node.left, new_level)
        insert(node.right, new_level)
    return new_level

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        lot = []
        while len(level) > 0:
            lot.append([node.val for node in level])
            level = step(level)
        return lot
    
        