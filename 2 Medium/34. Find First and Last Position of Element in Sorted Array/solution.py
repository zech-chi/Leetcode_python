class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                start = m
                r = m - 1
        
        end = -1
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                end = m
                l = m + 1
        
        return [start, end]
