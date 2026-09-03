class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l=[]
        l1=[]
        l2=[]
        l3=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                l.append(nums[i])
            elif nums[i]==pivot:
                l1.append(nums[i])
            else:
                l2.append(nums[i])
        l3=l+l1+l2
        return l3
        

        