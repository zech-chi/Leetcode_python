# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(arr):
            left = 0
            right = len(arr) - 1
            while (left < right):
                if (arr[left] and arr[right]):
                    if (arr[left].val != arr[right].val):
                        return False
                elif (not arr[left] and not arr[right]):
                    pass
                else:
                    return False
                left += 1
                right -= 1
            return True

        arr = [root]
        stop = False
        while (stop == False):
            if (not is_mirror(arr)):
                return False
            next_arr = []
            stop = True
            for node in arr:
                if (node):
                    next_arr.append(node.left)
                    next_arr.append(node.right)
                    stop = False
                else:
                    next_arr.append(None)
                    next_arr.append(None)
            arr = next_arr

        return True
