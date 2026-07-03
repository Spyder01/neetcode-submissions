from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        bag = defaultdict(int)
        box2 = defaultdict(int)

        for char in s:
            bag[char] += 1
        
        for char in t:
            box2[char] += 1
        
        for k, v in box2.items():
            if bag[k] != v:
                return False
        
        return True



        