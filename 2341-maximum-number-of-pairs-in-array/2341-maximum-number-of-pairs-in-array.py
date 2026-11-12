class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        c=0
        for i in range(len(nums)):
            if nums.count(nums[i])>=2 and nums[i] not in l:
                l.append(nums[i])
        k=[]
        for i in range(len(l)):
            if l[i] not in k:
                k.append(l[i])
                c+=nums.count(l[i])//2
        m=[]
        for i in range(len(l)):
            if nums.count(l[i])%2!=0:
                m.append(l[i])
        c_n=0
        n=[]
        for i in range(len(m)):
            if m[i] not in n:
                n.append(m[i])
                c_n+=1
        for i in range(len(nums)):
            if nums[i] not in l:
                c_n+=1
        return [c,c_n]



           
