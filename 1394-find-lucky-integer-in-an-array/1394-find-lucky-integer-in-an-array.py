class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        maxi=0
        for key,values in d.items():
            if key==values:
                maxi=max(key,maxi)
        if maxi==0:
            return -1
        return maxi
        