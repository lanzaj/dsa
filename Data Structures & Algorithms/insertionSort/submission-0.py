# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ret = []
        ret.append(pairs.copy())
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[i].key < pairs[j].key:
                pairs[i], pairs[j] = pairs[j], pairs[i]
                j -= 1
                i -= 1
            ret.append(pairs.copy())
        return ret