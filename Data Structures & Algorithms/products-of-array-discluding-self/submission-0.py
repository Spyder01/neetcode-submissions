class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hasZero = 0

        prod = 1

        for x in nums:
            if x == 0:
                hasZero += 1
            else:
                prod *= x

        res = []    
        for x in nums:
            if hasZero > 0 and x != 0:
                res.append(0)
                continue
            
            if x == 0 and hasZero > 1:
                res.append(0)
                continue

            
            if x == 0:
                x = 1
            
            res.append(prod//x)
        
        return res

        