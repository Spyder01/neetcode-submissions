class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True

        if len(s1) == 0 and s2 == s3:
            return True 
        
        if len(s2) == 0 and s1 == s3:
            return True

        def interleave(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k] and interleave(i+1, j, k+1):
                return True
            
            if j<len(s2) and s2[j] == s3[k] and interleave(i, j+1, k+1):
                return True
            
            return False

        return interleave(0,0,0)

        