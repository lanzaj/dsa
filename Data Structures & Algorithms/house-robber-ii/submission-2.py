class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(nums):
            prev1, prev2 = 0, 0
            for n in nums:
                tmp = max(prev1 + n, prev2)
                prev1 = prev2
                prev2 = tmp
            return prev2
                
        return max(rec(nums[1:]), rec(nums[:-1]))

