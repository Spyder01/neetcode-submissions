class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0:
            return [[]]

        nums.sort() 
        res = []

        def backtrack(index, subset):
            
            res.append(subset[:])

            if index == len(nums):
                return
            
            for i in range(index, len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue
                    
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

            
        backtrack(0, [])
        return res





        