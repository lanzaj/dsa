class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd=nums[0]
        minProd=1
        currProd = 1

        for n in nums:
            if currProd == 0:
                currProd = n
                minProd = n
            else:
                if n > 0 and currProd < 0:
                    currProd = n
                    minProd *= n
                else:
                    currProd *= n
                    minProd *= n
            maxProd = max(maxProd, currProd, minProd)
            print(currProd, minProd, maxProd)
        
        return maxProd
