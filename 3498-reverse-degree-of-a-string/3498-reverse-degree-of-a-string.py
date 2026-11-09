class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        for i in s:
            k=(ord('z')-ord(i))+1
            l.append(k)
        n=[]
        for i in range(len(l)):
            m=l[i]*(i+1)
            n.append(m)
        return sum(n)
            
