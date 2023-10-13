# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def LeftBinarySearchFindMinIndex(self, target: int, mountain_arr: 'MountainArray', right: int) -> int:
        start = -1
        l = 0
        r = right - 1
        while l <= r:
            m = (l + r) // 2
            val_at_m = mountain_arr.get(m)
            if val_at_m > target:
                r = m - 1
            elif val_at_m < target:
                l = m + 1
            else:
                start = m
                r = m - 1
        return start

    def RightBinarySearchFindMinIndex(self, target: int, mountain_arr: 'MountainArray', left: int) -> int:
        start = -1
        l = left
        r = mountain_arr.length() - 1
        while l <= r:
            m = (l + r) // 2
            val_at_m = mountain_arr.get(m)
            if val_at_m > target:
                l = m + 1
            elif val_at_m < target:
                r = m - 1
            else:
                start = m
                r = m - 1
        return start
    
    def BinarySearchFindTop(self, mountain_arr: 'MountainArray')-> int:
        l = 0
        r = mountain_arr.length() - 1
        while l <= r:
            m = (l + r) // 2
            val_at_left_m = mountain_arr.get(m - 1)
            val_at_m = mountain_arr.get(m)
            val_at_right_m = mountain_arr.get(m + 1)
            if val_at_left_m < val_at_m < val_at_right_m:
                l = m
            elif val_at_right_m < val_at_m < val_at_left_m:
                r = m
            else:
                return m

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        topMountain = self.BinarySearchFindTop(mountain_arr)
        ans = self.LeftBinarySearchFindMinIndex(target, mountain_arr, topMountain)
        if ans != -1:
            return ans
        ans = self.RightBinarySearchFindMinIndex(target, mountain_arr, topMountain)
        return ans
