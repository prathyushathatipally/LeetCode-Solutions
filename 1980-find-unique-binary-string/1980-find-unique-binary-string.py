class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        l=[]
        for i in range(2**len(nums)):
            k=bin(i)[2:]
            s=k.zfill(len(nums))
            l.append(s)
        w=[]
        for i in range(len(l)):
            if l[i] not in nums:
                w.append(l[i])
        return w[0]

        