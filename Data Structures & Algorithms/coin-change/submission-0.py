class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(coins, amount):
            if amount == 0:
                return 0
            if amount < 0 or len(coins) == 0:
                return -1
            res = rec(coins, amount - coins[-1])
            if res >= 0:
                return res + 1
            res = rec(coins[:-1], amount)
            if res >= 0:
                return res
            return -1
        return rec(coins, amount)