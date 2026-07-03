class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        cache = [0]*len(nums)
        
        def rob(index):
            if index >= len(nums):
                return 0

            # if (len(nums) - index)  in (1, 2):
                # return max(nums[index:])
            if cache[index] == 0:
                cache[index] =  max(nums[index] + rob(index + 2), rob(index+ 1))
            
            return cache[index]

        return rob(0) 

            


        