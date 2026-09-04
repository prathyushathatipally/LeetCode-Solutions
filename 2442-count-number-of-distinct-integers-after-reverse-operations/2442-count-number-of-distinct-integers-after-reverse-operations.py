class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            temp=nums[i]
            rev=0
            while temp>0:
                digits=temp%10
                rev=rev*10+digits
                temp=temp//10
            l.append(rev)
        k=nums+l
        l1=set()
        for i in range(len(k)):
            if k[i] not in l1:
                l1.add(k[i])
        return len(l1)
        