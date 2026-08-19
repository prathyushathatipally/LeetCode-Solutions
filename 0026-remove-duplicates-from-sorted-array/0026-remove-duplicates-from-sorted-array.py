class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
                count+=1
        for i in range(count):
            nums[i]=l[i] 
        return count        