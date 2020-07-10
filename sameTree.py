'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

'''

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None:
            return False

        if q is None:
            return False
        
        if p.value != q.value:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 