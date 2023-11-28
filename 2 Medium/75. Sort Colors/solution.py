class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min_j = i
            for j in range(i + 1, len(nums)):
                if (nums[j] < nums[min_j]):
                    min_j = j
            
            nums[i], nums[min_j] = nums[min_j], nums[i]
