class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=0
        num=x

        while x>0:
            digit=x%10
            a=a*10+digit
            x=x//10
        if num==a:
            return True
        else:
            return False
        