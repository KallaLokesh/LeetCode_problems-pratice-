class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        i=0
        while i<len(nums):
            count=0
            j=0
            while j<len(nums):
                if nums[j]<nums[i]:
                    count=count+1
                j=j+1
            ans.append(count)
            i=i+1
        return ans