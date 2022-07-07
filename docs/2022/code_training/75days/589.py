"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder_recursive(self, prelist: List[int], root: 'Node'):
        if root == None:
            return
        prelist.append(root.val)
        if root.children == None:
            return
        for ch in root.children:
            self.preorder_recursive(prelist, ch)

    def preorder(self, root: 'Node') -> List[int]:
        preorder_list = []
        self.preorder_recursive(preorder_list,root)
        return preorder_list
    
