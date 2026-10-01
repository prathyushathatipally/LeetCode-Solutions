class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        k=[]
        s=[]
        start=1
        end=len(nums)
        for i in range(start,end+1):
            l.append(i)
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in l:
            if i not in d:
                k.append(i)
        for i in d:
            if d[i]==2:
                s.append(i)
        return s+k


        
            
        