class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        total=0
        for i in accounts:
            a=sum(i)
            if a>total:
                total=a
        return total
