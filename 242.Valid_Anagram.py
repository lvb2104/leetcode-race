class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ls = [0] * 123
        for i in range(len(s)):
            ls[ord(s[i])] += 1
            ls[ord(t[i])] -= 1

        for num in ls:
            if num != 0:
                return False
        
        return True