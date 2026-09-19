class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # k=sorted(nums)
        # l=[]
        # for i in range(len(k)):
        #     if k[i] not in l:
        #         l.append(k[i])
        # return l
    
        k=0
        m=set(nums)
        for i in m:
            if i-1 not in m:
                current=i
                c=1
                while current+1 in m:
                    current=current+1
                    c+=1
                k=max(c,k)
        return k



        