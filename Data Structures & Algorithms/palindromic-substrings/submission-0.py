class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.rec(s, i, i)
            res += self.rec(s, i, i + 1)
        return res
        
    def rec(self, s, start, finish):
        res = 0
        while start >= 0 and finish < len(s) and s[start] == s[finish]:
            start -= 1
            finish += 1
            res += 1
        return res

        