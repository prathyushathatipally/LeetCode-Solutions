class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        m=int("".join(map(str,num)))
        s=m+k
        n=list(map(int,str(s)))
        return n
        