class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        res = 1
        i = 0
        while i < len(s):
            if s[i] == "0":
                return 0
            if s[i] <= "2":
                if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] < "7"):
                    if s[i+1] == "0":
                        i += 1
                        if s[i+1] == "0":
                            return 0
                    else:
                        if i+2 == len(s) or s[i+2] != "0":
                            res += 1
            i += 1
        return res



        