class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        i = 0
        while i < len(s):
            length_word = 0
            while '0' <= s[i] <= '9':
                length_word = length_word * 10 + int(s[i])
                i += 1
            i += 1
            for _ in range(0, length_word):
                cur = cur + s[i]
                i += 1
            
            res.append(cur)
            cur = ""
            
        return res

