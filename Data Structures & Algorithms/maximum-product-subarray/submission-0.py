class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd=nums[0]
        maxProd=nums[0]
        currProd = 1

        for n in nums:
            if currProd == 0:
                currProd = n
            else:
                if n > 0 and currProd < 0:
                    currProd = n
                else:
                    currProd *= n
            minProd = min(minProd, currProd)
            maxProd = max(maxProd, currProd)
            print(currProd, minProd, maxProd)
        
        return maxProd
