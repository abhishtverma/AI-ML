class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        b=0
        original=x
        while x !=0:
         a = x % 10
         b = b * 10 + a
         x = x // 10
        if(b==original):
         return True
        else:
         return False
    