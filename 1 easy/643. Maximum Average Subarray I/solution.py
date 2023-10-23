class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        Max_sum = window_sum
        l = 0
        for r in range(k, len(nums)):
            window_sum += (nums[r] - nums[l])
            Max_sum = max(Max_sum, window_sum)
            l += 1
        
        return Max_sum / k
