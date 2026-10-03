class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for key in d:
            if d[key]>len(nums)/3:
                l.append(key)
        return l

        