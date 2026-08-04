class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        a=sum(nums[:k])
        max_sum=a
        for i in range(k,len(nums)):
            a=a+nums[i]-nums[i-k]
            if a>max_sum:
                max_sum=a
        return (float(max_sum)/k)