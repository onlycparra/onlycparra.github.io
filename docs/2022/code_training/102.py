# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return None
        this_level = [root]
        next_level = []
        traversal_all = []
        while this_level:
            traversal_this_level = []
            while this_level:
                # unqueue the next node in this level
                uncle = this_level.pop(0)
                traversal_this_level.append(uncle.val)

                # queue childs to the next level
                if uncle.left:
                    next_level.append(uncle.left)
                if uncle.right:
                    next_level.append(uncle.right)
                    
            # add this level to the master list.
            traversal_all.append(traversal_this_level)
            
            # next level becomes this level
            this_level,next_level = next_level,this_level

        return traversal_all
