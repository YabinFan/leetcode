# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, running_sum, path, all_paths):
        if not root:
            return []
        new_running_sum = running_sum-root.val
        if not root.left and not root.right and new_running_sum == 0:
            all_paths.append(path)
        if root.left:
            self.dfs(root.left, new_running_sum, path+[root.left.val], all_paths)
        
        if root.right:
            self.dfs(root.right, new_running_sum, path+[root.right.val], all_paths)
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        all_paths = []
        self.dfs(root, targetSum, [root.val], all_paths)
        return all_paths
