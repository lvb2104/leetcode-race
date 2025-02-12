class Solution:
    def isPalindrome(self, x: int) -> bool:
        test = x
        reverse = 0
        while test > 0:
            reverse = (reverse * 10) + (test % 10)
            test //= 10
        return x == reverse