class Solution:
    def rec(self, nums, first_selected):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if first_selected else nums[0]
        if len(nums) == 2:
            return nums[0] if first_selected else max(nums[0], nums[1])
        else:
            return max(nums[0] + self.rec(nums[2:], first_selected), self.rec(nums[1:], first_selected))

    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.rec(nums[2:], True), self.rec(nums[1:], False))

