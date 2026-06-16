class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(t) != len(s):
            return False
        
        for i in range(len(s)) and range(len(t)):
            if(s[i] != t[i]):
                return False
        
        return True

        