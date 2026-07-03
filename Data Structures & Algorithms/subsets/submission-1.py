class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []

        def backtrack(index, subset):
            res.append(subset[:])

            if index == len(nums) or len(subset) == len(nums):
                return
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()
            

        backtrack(0, [])
        return res



        

