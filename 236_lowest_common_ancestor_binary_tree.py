# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None} # node---->parent
        
        # loop over until we find both p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        # all the parents of p
        ancestors_p = set()
        
        while p:
            ancestors_p.add(p)
            p = parent[p]
        
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.  
        while q not in ancestors_p:
            q = parent[q]
        return q
