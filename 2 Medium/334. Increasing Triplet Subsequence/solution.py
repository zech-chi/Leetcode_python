class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        i1 = float('inf')
        i2 = float('inf')

        for i3 in nums:
            if i3 <= i1:
                i1 = i3
            elif i3 <= i2:
                i2 = i3
            else:
                return True

        return False
