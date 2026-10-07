class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = 0

            # first window
        for i in range(k):
            s += nums[i]

        maxi = s

            # slide the window
        for i in range(k, len(nums)):
            s = s - nums[i-k]
            s = s + nums[i]

            if s > maxi:
                maxi = s

        return maxi / float(k)            