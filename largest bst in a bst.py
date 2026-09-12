''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def largestBst(self, root: 'Node') -> int:
        def postorder(node):
            # Your code here
            if not node:
                return float("inf"),float("-inf"),0
                
            left_min,left_max,left_sz=postorder(node.left)
            right_min,right_max,right_sz=postorder(node.right)
            
            #this is if it is a valid bst
            if left_max <node.data <right_min:
                return(
                    min(node.data,left_min),
                    max(node.data,right_max),
                    left_sz+right_sz+1,
                    )
            #if not a bst
            return float("-inf"),float("inf"),max(left_sz,right_sz)
        return postorder(root)[2]
                    