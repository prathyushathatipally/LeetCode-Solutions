class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            temp=nums[i]
            while temp>0:
                digits=temp%10
                l.append(digits)
                temp=temp//10
        c=0
        for i in range(len(l)):
            if l[i]==digit:
                c+=1
        return c
        