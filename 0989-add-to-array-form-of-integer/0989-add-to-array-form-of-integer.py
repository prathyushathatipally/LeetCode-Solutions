class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=[]
        total=0
        num=int("".join(map(str,num)))
        total=num+k
        k=list(map(int,str(total)))
        return k
    



       