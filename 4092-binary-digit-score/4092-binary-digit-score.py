class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l=""
        m=bin(a)[2:]
        n=bin(b)[2:]
        s=m.count("1")
        k=n.count("1")
        if s>k or s==k:
            l=s*k
        if s<k:
            l=k/s
        return l
        