class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            k=1
            temp=n
            while temp>0:
                digits=temp%10
                k*=digits
                temp=temp//10
                if k%t==0:
                    return n
            n+=1
        return n


        