class Solution:
    def numDecodings(self, s: str) -> int:
        dp1, dp2 = 1, 0
        
        for i in range(len(s) - 1, -1, -1):
            tmp = 0
            if s[i] == "0":
                tmp = 0
            else:
                tmp = dp1

            if i + 1 < len(s) and (
                s[i] == "1" or
                s[i] == "2" and s[i + 1] in "0123456"
            ):
                tmp += dp2
            dp2 = dp1
            dp1 = tmp
        return dp1

############### ITERATIF ##############
        # dp = {len(s) : 1}
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == "0":
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]

        #     if i + 1 < len(s) and (
        #         s[i] == "1" or
        #         s[i] == "2" and s[i + 1] in "0123456"
        #     ):
        #         dp[i] += dp[i + 2]
        # return dp[0]

############ RECURSIF ###############
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
            
        #     res = dfs(i + 1)
        #     if i + 1 < len(s) and (
        #         s[i] == "1" or
        #         s[i] == "2" and s[i + 1] in "0123456"
        #     ):
        #         res += dfs(i + 2)
        #     dp[i] = res
        #     return res
        # return dfs(0)




        