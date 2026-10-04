class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        l=[]
        for i in range(left,right+1):
            l.append(bin(i)[2:])
        s=[]
        for i in range(len(l)):
            k=l[i].count("1")
            s.append(k)
        c=0
        for i in range(len(s)):
            d=0
            for j in range(1,s[i]+1):
                if s[i]%j==0:
                    d+=1
            if d==2:
                c+=1
        return c

        



        