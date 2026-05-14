class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount in dp:
                return dp[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            minCoin = float('inf')
            for coin in coins:
                res = dfs(amount - coin)
                if res >= 0 and res + 1 < minCoin:
                    minCoin = res + 1
            
            dp[amount] = minCoin if minCoin != float('inf') else -1
            return dp[amount]

        return dfs(amount)
