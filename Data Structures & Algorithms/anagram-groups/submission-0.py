class Solution:
    def isAnagram(self, a: str, b: str):
        if len(a) != len(b):
            return False

        bag1 = {}
        bag2 = {}

        for char in a:
            if char not in bag1:
                bag1[char] = 0

            bag1[char] += 1

        for char in b:
            if char not in bag2:
                bag2[char] = 0

            bag2[char] += 1
        
        for char, count in bag1.items():
            if char not in bag2:
                return False

            if bag2[char] != count:
                return False
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        
        if len(strs) == 1:
            return [strs]

        res = []
        char = {}
        for i, x in enumerate(strs):
            if x in char:
                continue
                
            bag = [x]
            for b in strs[i + 1:]:
                if self.isAnagram(x, b):
                    char[b] = True
                    bag.append(b)
                
            
            res.append(bag)

        return res