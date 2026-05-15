class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        res = 0
        for n in nums:
            #print(dp)
            maxLen = 1
            for m in dp:
                if m < n:
                    maxLen = max(maxLen, dp[m] + 1)
            dp[n] = maxLen
            res = max(maxLen, res)

        return res  
                