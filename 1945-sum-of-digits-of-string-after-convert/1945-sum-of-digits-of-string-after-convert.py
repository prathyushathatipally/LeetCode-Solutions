class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m=0
        l=[]
        t=list(map(str,s))
        for i in range(len(t)):
            m=ord(t[i])-ord('a')+1
            l.append(m)
        f=int("".join(map(str,l)))
        for i in range(k):
            s=0
            while f>0:
                digits=f%10
                s+=digits
                f=f//10
            f=s
        return s
        