class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        def is_palindrome(s):
            return s[::-1] == s
        
        start, pointer = 0, 0

        res = ""

        for i in range(len(s)):
            for pointer in range(i, len(s) + 1):
                word = s[i:pointer]
                print(word)
    
                if is_palindrome(word):
                    if len(res) < len(word):
                        res = word
    
                pointer += 1
            
        
        return res
            

        