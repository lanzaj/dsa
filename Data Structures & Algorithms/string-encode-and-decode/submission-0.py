class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + string + "encode"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        i = 0
        while i < len(s):
            if i + 6 <= len(s) and s[i:i+6] == "encode":
                res.append(cur)
                cur = ""
                i += 6
            else:
                cur = cur + s[i]
                i += 1
        return res

