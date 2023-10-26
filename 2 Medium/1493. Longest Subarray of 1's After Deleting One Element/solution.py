class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left_sum = [0] * len(nums)
        left_sum[0] = nums[0]
        exist_zero = False
        if nums[0] == 0:
            exist_zero = True

        for i in range(1, len(nums)):
            if nums[i] == 1:
                left_sum[i] = left_sum[i - 1] + 1
            else:
                exist_zero = True

        if exist_zero == False:
            return left_sum[-1] - 1
        
        right_sum = [0] * len(nums)
        right_sum[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 1:
                right_sum[i] = right_sum[i + 1] + 1

        Max = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if i == 0:
                    cur_sum = right_sum[i + 1]
                elif i == len(nums) - 1:
                    cur_sum = left_sum[i - 1]
                else:
                    cur_sum = left_sum[i - 1] + right_sum[i + 1]
                
                Max = max(Max, cur_sum)
        return Max
