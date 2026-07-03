class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        def backtrack(index, combination, target):
            if target == 0:
                result.append(combination[:])
                return

            if target < 0 or index >= len(nums):
                return
            
            x = nums[index]
            combination.append(x)
            backtrack(index, combination, target - x)
            combination.pop()
            backtrack(index + 1, combination, target)
            
        backtrack( 0, [], target)
        return result 
        