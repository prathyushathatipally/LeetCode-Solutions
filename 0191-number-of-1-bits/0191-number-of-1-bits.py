class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        s=bin(n)[2:]
        r=str(s)
        for i in s:
            if i=='1':
                c+=1
        return c



        