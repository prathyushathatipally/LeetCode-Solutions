class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k=2*n
        l=3*n
        s=str(n)+str(k)+str(l)
        if len(s)==9 and set(s)==set("123456789"):
            return True
        return False






        