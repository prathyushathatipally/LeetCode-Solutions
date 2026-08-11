class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        l = []

        i = 0
        j = len(nums) - 1

        while i < j:
            k = nums[i] + nums[j]
            avg = k / 2.0
            l.append(avg)

            i += 1
            j -= 1

        l1 = []
        c = 0

        for i in range(len(l)):
            if l[i] not in l1:
                l1.append(l[i])
                c += 1

        return c
        # k=""
        # avg=""
        # l=[]
        # s=sorted(nums)
        # for i in range(len(nums)//2):
        #     k=nums[i]+nums[len(nums)-1-i]
        #     avg=k/2.0
        #     l.append(avg)
        # l1=[]
        # for i in l:
        #     if i not in l1:
        #         l1.append(i)
        # return len(l1)






        