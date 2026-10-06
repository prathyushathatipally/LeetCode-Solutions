class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        l=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                l.append(nums[i])
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        maxi=0
        ans=0
        if len(l)==0:
            return -1
        for key,values in d.items():
            if values>maxi:
                maxi=values
                ans=key
            elif values==maxi and key<ans:
                ans=key
        return ans


        