'''Structure of a Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthLargest(self, root, k):
        # code here
        stack=[]
        curr=root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.right
            curr=stack.pop()
            k-=1
            if k==0:
                return curr.data
            curr=curr.left
        return -1
        