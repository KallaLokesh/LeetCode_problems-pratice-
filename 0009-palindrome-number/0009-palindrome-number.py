class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse=""
        num=str(x)
        for i in str(x):
            reverse=i+reverse
            
        if num==reverse:
            return True
        else:
            return False
        