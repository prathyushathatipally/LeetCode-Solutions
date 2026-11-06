class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=[]
        for i in range(len(nums)):
            l.append(bin(nums[i])[2:])
        k=[]
        c=0
        for i in range(len(l)):
            if l[i][-1]=="0":
                c+=1
                if c>=2:
                    return True
        return False
        