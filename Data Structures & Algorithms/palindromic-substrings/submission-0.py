class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        if len(s) == 2:
            if s[1] == s[0]:
                return 3
            return 2
        
        count = 0

        for i in range(len(s)):
            p, q = i, i

            while p >= 0 and q < len(s):
                if s[p] != s[q]:
                    break
                
                count += 1
                p -= 1
                q += 1
        
            p, q = i, i + 1

            while p >= 0 and q < len(s):
                if s[p] != s[q]:
                    break
                
                count += 1
                p -= 1
                q += 1
        return count

        
        
        