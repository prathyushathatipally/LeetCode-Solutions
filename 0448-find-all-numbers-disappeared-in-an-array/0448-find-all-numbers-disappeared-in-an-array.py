class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        start=1
        end=len(nums)
        s=set(nums)
        for i in range(start,end+1):
            if i not in s:
                l.append(i)
        return l

        