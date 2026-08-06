class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        i=0
        while i<n:
            ans.append(nums[i])
            ans.append(nums[i+n])
            i=i+1
        return ans