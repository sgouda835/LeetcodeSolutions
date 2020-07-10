'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(root, minValue, maxValue):
        if root is None:
            return True
        
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        return self.helper(root.left, minValue, root.val) and self.helper(root.right, root.val, maxValue) 






