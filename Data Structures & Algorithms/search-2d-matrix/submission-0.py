class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = []

        for x in matrix:
            arr = [*arr, *x]

        l, r = 0, len(arr) - 1 

        while l<=r:
             mid = (l+r)//2

             num = arr[mid]

             if num == target:
                return True

             if num < target:
                l += 1
             else:
                r -= 1
        
        return False
