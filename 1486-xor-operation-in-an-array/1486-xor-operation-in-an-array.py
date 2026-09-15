class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        l=[]
        for i in range(n):
            nums=start+2*i
            l.append(nums)
        s=0
        for i in range(len(l)):
            s=s^l[i]
        return s


        