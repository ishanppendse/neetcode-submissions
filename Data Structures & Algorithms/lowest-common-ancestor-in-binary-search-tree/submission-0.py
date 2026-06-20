# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search(node, x, path):
    path.append(node)
    if node.val == x:
        return path
    elif node.val < x:
        return search(node.right, x, path)
    else:
        return search(node.left, x, path)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        trace_p = search(root, p.val, list([]))
        trace_q = search(root, q.val, list([]))
        pointer_p = 0
        pointer_q = 0
        while pointer_p < len(trace_p) and pointer_q < len(trace_q):
            if trace_p[pointer_p].val != trace_q[pointer_q].val:
                break
            pointer_p += 1
            pointer_q += 1
        return trace_p[pointer_p-1]
        