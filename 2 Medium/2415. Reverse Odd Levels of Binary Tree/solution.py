# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        cur_nodes = [root]
        while cur_nodes[0]:
            next_nodes = []
            for node in cur_nodes:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            
            if (level % 2):
                left = 0
                right = len(cur_nodes) - 1
                while (left < right):
                    temp = cur_nodes[left].val
                    cur_nodes[left].val = cur_nodes[right].val
                    cur_nodes[right].val = temp
                    left += 1
                    right -= 1
            
            cur_nodes = next_nodes
            level += 1
        
        return root
