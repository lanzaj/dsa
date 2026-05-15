class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            minCoin = float('inf')
            for coin in coins:
                if amount - coin in dp:
                    res = dp[amount - coin]
                else:
                    res = dfs(amount - coin)
                if res >= 0:
                    dp[amount] = res + 1
                    minCoin = res + 1
            if minCoin != float('inf'):
                return minCoin
            return -1

        return dfs(amount)
        

    
