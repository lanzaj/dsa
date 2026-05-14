class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = ""
        for i in range(len(s)):
            pal = self.helper(s, i, i)
            longestPal = pal if len(pal) > len(longestPal) else longestPal
            pal2 = self.helper(s, i, i + 1)
            longestPal = pal2 if len(pal2) > len(longestPal) else longestPal
        return longestPal
        
    def helper(self, s, start, finish):
        res = ""
        while start >= 0 and finish < len(s) and s[start] == s[finish]:
            res = s[start:finish+1]
            start -= 1
            finish += 1
        return res

        