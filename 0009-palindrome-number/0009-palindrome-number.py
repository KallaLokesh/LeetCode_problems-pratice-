class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        sum1=0
        n=x
        while x>0:
            temp=x%10
            sum1=sum1*10+temp
            x//=10
        if n==sum1:return True
        else:return False
        