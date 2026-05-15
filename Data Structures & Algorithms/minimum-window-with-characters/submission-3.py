class Solution:

    def removeChar(self, c, subString):
        if c in subString and subString[c] > 0:
            subString[c] -= 1
            self.have -= 1
            print(c)
        
    def addChar(self, c, subString, t_count):
        if c not in t_count:
            return
        if c not in subString:
            subString[c] = 1
        else:
            subString[c] += 1
        self.have += 1

    # def checkS(self, s, t):
    #     for c in t:
    #         if (c not in s or s[c] < t[c]):
    #             return False
    #     return True


    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        subString = {}
        shortestString = (-1, 10001)

        l = 0
        r = 0

        self.have = 0
        self.need = 0

        for c in t_count:
            self.need += t_count[c]
        self.addChar(s[0], subString, t_count)

        while r < len(s):
            while not (self.need == self.have) and r < len(s):
                r += 1
                if (r < len(s)):
                    self.addChar(s[r], subString, t_count)
            while self.need == self.have and l <= r:
                if shortestString[1] - shortestString[0] > r - l:
                    shortestString = (l, r)
                self.removeChar(s[l], subString)
                l += 1
        
        if shortestString == (-1, 10001):
            return ""
        return s[shortestString[0]: shortestString[1]+1]

        
