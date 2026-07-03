class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_ = 0
        n = len(heights)

        i, j = 0, n - 1

        while i < j:
            area = abs(min(heights[i], heights[j]) * (j - i))

            if area > max_:
                max_ = area
            
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_
        
        