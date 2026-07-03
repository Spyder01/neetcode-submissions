class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return [[]]
        
        res, part = [], []
        def backtrack(index: int = 0):
            if index >= len(s):
                res.append(part[:])
                return
            
            if index == len(s):
                return
            
            for i in range(index, len(s)):
                word = s[index : i+1]
                if word != word[::-1]:
                    continue
                    
                part.append(s[index : i+1])
                backtrack(i+1)
                part.pop()
            
        backtrack()

        return res
        