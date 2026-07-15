class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        sum=0
        while (num):
            temp=num%10
            sum+=temp
            num=num//10
        return self.addDigits(sum)  