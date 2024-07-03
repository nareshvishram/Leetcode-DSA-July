class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        if n<5:
            return 0
        return min(nums[n-4]-nums[0],nums[n-3]-nums[1],nums[n-2]-nums[2],nums[n-1]-nums[3])
        