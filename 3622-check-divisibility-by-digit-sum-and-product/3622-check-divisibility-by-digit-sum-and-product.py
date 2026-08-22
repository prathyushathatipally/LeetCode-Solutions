class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=0
        temp=n
        p=1
        t=0
        while temp>0:
            digits=temp%10
            s+=digits
            p*=digits
            temp=temp//10
        t=s+p
        if n%t==0:
            return True
        return False
        

        


        