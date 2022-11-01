# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class Range:
        def __init__(self, Min, Max):
            self.Min = Min
            self.Max = Max
            
    def getTreeRange(self, root: TreeNode) -> Optional[Range]:
        myRange = Range(root.val, root.val)
        
        # If the left tree exists, then we test for correctness and update myRange
        # to reflect the minimum of the whole tree.
        if root.left != None:
            branchRange = self.getTreeRange(root.left)
            # if the left tree was incorrect, or the max of the left tree is equal
            # or greater than the root's value, then this tree is not a BST
            if branchRange == None or branchRange.Max >= myRange.Min:
                return None
            myRange.Min = branchRange.Min

        # Same idea with the right tree
        if root.right != None:
            branchRange = self.getTreeRange(root.right)
            if branchRange == None or branchRange.Min <= myRange.Max:
                return None
            myRange.Max = branchRange.Max

        return myRange
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None or self.getTreeRange(root) != None:
            return True

