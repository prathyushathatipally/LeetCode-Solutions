class Solution(object):
    def validDigit(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: bool
        """
        temp=n
        l=[]
        while temp>0:
            digits=temp%10
            l.append(digits)
            temp=temp//10
        k=l[::-1]
        if x in k and k[0]!=x:
            return True
        return False




        
        