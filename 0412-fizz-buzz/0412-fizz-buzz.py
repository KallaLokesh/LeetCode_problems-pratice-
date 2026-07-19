class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sum=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                sum.append("FizzBuzz")
            elif i%3==0:
                sum.append("Fizz")
            elif i%5==0:
                sum.append("Buzz")
            else:
                sum.append(str(i))
        return sum