class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        for i in nums:
            l=[]
            while i>0:
                digits=i%10
                l.append(digits)
                i=i//10
            result.append(l)
        ranges=[]
        for i in result:
            largest=max(i)
            smallest=min(i)
            Digit_Range=largest-smallest
            ranges.append(Digit_Range)
        maximum=max(ranges)
        k=[]
        s=0
        for i in range(len(ranges)):
            if ranges[i]==maximum:
                k.append(nums[i])
                s=sum(k)
        return s
            

        

      

