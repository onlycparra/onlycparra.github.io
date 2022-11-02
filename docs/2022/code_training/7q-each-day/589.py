"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    # Recursive Solution
    def __init__(self):
        self.preorder_list = []*1000
        
    def preorder_rec(self, root: 'Node') -> None:
        self.preorder_list.append(root.val)
        for c in root.children:
            self.preorder_rec(c)
        return
        
    def preorder(self, root: 'Node') -> List[int]:
        if root != None:
            self.preorder_rec(root)
        return self.preorder_list
