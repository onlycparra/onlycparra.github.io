# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        uncles = [root]
        answer = []
        while len(uncles) > 0:
            nephews = []
            level_vals = []

            # passing through one generation.
            while len(uncles) > 0:
                dady = uncles.pop(0)
                level_vals.append(dady.val)
                if dady.left != None:
                    nephews.append(dady.left)
                if dady.right != None:
                    nephews.append(dady.right)
            answer.append(level_vals)
            uncles, nephews = nephews, uncles

        return answer
