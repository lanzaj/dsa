class Solution:
    def findMin(self, nums: List[int]) -> int:
        M = len(nums)
        min = nums[M % len(nums)]
        i = 0

        while M != 0:
            M = M // 2
            if nums[i % len(nums)] < min:
                i -= M
                min = nums[i % len(nums)]
            else:
                i += M
        
        return min
