class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for values in d.values():
            c=0
            for i in range(1,values+1):
                if values%i==0:
                    c+=1
            if c==2:
                return True
        return False