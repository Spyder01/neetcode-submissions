class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        box = set()

        for num in nums:
            if num in box:
                return True
            
            box.add(num)
        
        return False
