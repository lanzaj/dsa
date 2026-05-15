class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def rec(i):
            if i == 0:
                return True
            for jump_size in range(i, 0, -1):
                if nums[i - jump_size] >= jump_size:
                    if rec(i - jump_size):
                        return True
            return False
        
        return rec(len(nums) - 1)