class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        alphabets = set()
        for i in range(1, 27):
            alphabets.add(str(i))

        if s[0] not in alphabets:
            return 0

        if len(s) == 1:
            return 1

        res = 0
        if len(s) == 2:
            if s in alphabets:
                res += 1
            
            if s[1] in alphabets:
                res += 1
            return res

        if s[:2] in alphabets:
            res = self.numDecodings(s[2:])

        res += self.numDecodings(s[1:])
        return res

        