class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        for i in range(len(s) + 1):
            dp[i] = False
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                start = i - len(word)
                if start >= 0:
                    # print(i, word, start, s[start:i], dp[start])
                    tmp = (s[start:i] == word and dp[start])
                    if tmp:
                        dp[i] = tmp
                    
        return dp[len(s)]
                    
                