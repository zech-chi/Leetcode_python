class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        Sum = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                Sum += nums[i]
        return (Sum)
