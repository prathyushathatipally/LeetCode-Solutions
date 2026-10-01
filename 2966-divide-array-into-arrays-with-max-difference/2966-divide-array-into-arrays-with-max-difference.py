class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        s=sorted(nums)
        l=[]
        for i in range(0,len(nums),3):
            if s[i+2]-s[i]<=k:
                l.append([s[i],s[i+1],s[i+2]])
            else:
                return []
        return l

        