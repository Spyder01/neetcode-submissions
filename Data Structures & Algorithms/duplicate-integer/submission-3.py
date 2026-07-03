class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        marked = set()

        for num in nums:
            if num in marked:
                return True
            
            marked.add(num)
        
        return False
        