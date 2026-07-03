class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        i, j = 0, n -1

        while j >= i:

            sum_ = numbers[i] + numbers[j]

            if sum_ == target:
                return [i+1, j+1]
            
            if sum_ < target:
                i += 1
            
            if sum_ > target:
                j -= 1
        
        return []

        