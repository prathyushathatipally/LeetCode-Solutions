class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=0
        odd_freq=0
        even_freq=0
        l=list(s)
        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        l1=[]
        for key,values in d.items():
            if values%2==0:
                l.append(values)
            else:
                l1.append(values)
        s=max(l1)
        m=min(l)
        return s-m
