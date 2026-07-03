class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        prod = - 2 ** 31

        for i in range(len(nums)):
            _prod = 1
            for j in range(i, len(nums)):
                _prod *= nums[j]

                prod = max(_prod, prod)
        
        return prod

        