"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # Iterative Solution
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        expansion_stack = [root]
        preorder_list = []
        while len(expansion_stack) > 0:
            curr_node = expansion_stack.pop()
            preorder_list.append(curr_node.val)
            expansion_stack.extend(reversed(curr_node.children))
            
        return preorder_list
