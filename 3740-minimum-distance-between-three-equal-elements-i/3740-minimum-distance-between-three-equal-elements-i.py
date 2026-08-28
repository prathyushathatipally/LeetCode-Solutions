class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        k=abs(i-j)+abs(j-k)+abs(k-i)
                        l.append(k)
        if l:
            s=min((l))
            return s
        return -1