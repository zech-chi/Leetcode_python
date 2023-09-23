class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = nums[0][1] - nums[0][0] + 1
        max_end = nums[0][1]
        for i in range(1, len(nums)):
            if max_end >= nums[i][1]:
                pass
            elif nums[i][0] <= max_end < nums[i][1]:
                res += nums[i][1] - max_end
                max_end = nums[i][1]
            else:
                res += nums[i][1] - nums[i][0] + 1
                max_end = nums[i][1]
        return res
