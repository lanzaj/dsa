# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSort2(pairs, 0, len(pairs) - 1)

    def mergeSort2(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1: #1 - 0 + 1 <= 1
            return pairs
        
        m = int((e + s) / 2)
        self.mergeSort2(pairs, s, m)
        self.mergeSort2(pairs, m + 1, e)

        return self.merge(pairs, s, m, e)


    def merge(self, pairs: List[Pair], s: int, m: int, e: int) -> List[Pair]:
        p1 = pairs[s:m+1]
        p2 = pairs[m+1:e+1]
        i1 = 0
        i2 = 0
        for i in range(s, e + 1):
            if i1 < len(p1) and (i2 >= len(p2) or p1[i1].key <= p2[i2].key):
                pairs[i] = p1[i1]
                i1 += 1
            elif i2 < len(p2):
                pairs[i] = p2[i2]
                i2 += 1
        return pairs
